import struct
import time
from typing import List, Dict

from serial import Serial

from constants.channel_info import channel_info as get_channel_info
from constants import channels
from constants import hd_data_types
from constants.hd_data_types import ChannelDataType, ChannelSizeType, ch_data_convert

DL_GetDatalogInfo = 0x30
DL_GetDatalogChannelIDs = 0x31
DL_GetDatalogPacket = 0x35

datalog_info = bytes.fromhex('00 30 08 00 32 00 3B 00')

channel_info = bytes.fromhex('00 31 9A 00 00 01 83 01 01 84 02 01 42 20 01 47 10 01 85 11 02 49 10 02 49 30 01 88 40 01 89 50 01 50 60 01 50 70 01 46 80 01 59 00 02 41 01 02 41 00 03 58 10 03 58 20 03 9E 22 03 9E 30 03 52 32 03 52 40 03 41 11 04 89 12 04 51 10 04 4B 00 04 58 20 04 82 01 05 41 02 05 41 03 05 41 04 06 41 05 05 41 06 05 58 01 06 41 02 06 41 03 06 41 07 06 41 00 07 41 30 07 51 00 08 41 01 08 41 10 08 41 11 08 41 20 08 41 21 08 41 12 0A 51 30 0A 4B 31 0A 42 03 0B 51 04 0B 50')

datalog_packet = bytes.fromhex('00 35 3F 00 00 00 00 00 00 13 E8 03 14 14 00 00 14 00 60 73 C4 7A 00 00 00 D2 00 80 00 80 80 7A 00 14 00 2B 00 00 00 00 00 00 00 00 01 BE 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 20')


class HondataPacket:
    def __init__(self, packet):
        self.packet = packet
        self.protocol, self.id, self.size = struct.unpack('<BBH', packet[:4])
        self.payload = packet[4:]

    @staticmethod
    def packet_factory(packet: bytes):
        _hd_packet = HondataPacket(packet)
        if _hd_packet.id == DL_GetDatalogInfo:
            return DatalogInfoPacket(packet)
        elif _hd_packet.id == DL_GetDatalogChannelIDs:
            return DatalogChannelInfoPacket(packet)
        elif _hd_packet.id == DL_GetDatalogPacket:
            return DatalogPacket(packet)


class DatalogInfoPacket(HondataPacket):
    DL_GetDatalogInfo = 0x30

    def __init__(self, packet: bytes):
        super(DatalogInfoPacket, self).__init__(packet)
        self.channel_count, self.dl_packet_size = struct.unpack('<HH', self.payload)


class DatalogChannelInfoPacket(HondataPacket):
    DL_GetDatalogChannelIDs = 0x31

    def __init__(self, packet: bytes):
        super(DatalogChannelInfoPacket, self).__init__(packet)
        self.channels = {}

    def parse_channels(self, size: int):
        # assert len(self.payload) == size, "Channel packet size and Channel list sizes differ"
        offset = 0
        for i in range(0, int(len(self.payload)/3)):
            CID, sizeType = struct.unpack('<HB', self.payload[offset:offset+3])
            channel_name = get_channel_info[CID]
            self.channels[i] = DatalogChannel(CID, sizeType, channel_name)
            offset = offset+3
        return


class DatalogChannel:
    def __init__(self, CID, sizeType, name):
        self.CID = CID
        self.size = ChannelSizeType(sizeType & ChannelSizeType.CS_MASK.value)
        self.type = ChannelDataType(sizeType & ChannelSizeType.CT_MASK.value)
        self.name = name


class DatalogPacket(HondataPacket):
    def __init__(self, packet: bytes):
        super(DatalogPacket, self).__init__(packet)
        self.datalog_dict = {}

    def parse_datalog(self, channel_list: Dict[int, DatalogChannel]):
        offset = 0
        for i in range(0, len(channel_list)):
            if channel_list[i].size == ChannelSizeType.CS_BYTE:
                raw_val, = struct.unpack('<B', self.payload[offset:offset+1])
                offset+=1
            elif channel_list[i].size == ChannelSizeType.CS_WORD:
                raw_val, = struct.unpack('<H', self.payload[offset:offset+2])
                offset+=1
            else:
                raw_val = None
                print("size not found")

            self.datalog_dict[channel_list[i].name] = ch_data_convert[channel_list[i].type](raw_val)
        return

# class ChannelInfo:
#     def __init__(self, packed_info):
#         pass

if __name__ == '__main__':
    dev = Serial('COM13', 115200)
    dev.read_all()
    dev.write(bytes([0x00, DL_GetDatalogInfo, 0x04, 0x00]))
    datalog_info = b''
    while not dev.in_waiting:
        time.sleep(.01)
    while dev.in_waiting:
        datalog_info+=dev.read(dev.in_waiting)

    dl_info = DatalogInfoPacket(datalog_info)
    dev.write(bytes([0x00, DL_GetDatalogChannelIDs, 0x04, 0x00]))
    channel_info = b''
    while not dev.in_waiting:
        time.sleep(.01)
    while dev.in_waiting:
        channel_info+=dev.read(dev.in_waiting)

    dl_chan_info = DatalogChannelInfoPacket(channel_info)
    dl_chan_info.parse_channels(dl_info.dl_packet_size)
    input("Connected. press any key to datalog.")
    datalog = {}
    log_file = open(f'datalog_{time.time_ns()}.log', 'a')
    log_file.write("DATALOG_START\n")
    while True:
        try:
            dev.write(bytes([0x00, DL_GetDatalogPacket, 0x04, 0x00]))
            datalog_packet = b''
            while not dev.in_waiting:
                time.sleep(.01)
            while dev.in_waiting:
                datalog_packet += dev.read(dev.in_waiting)
        except:
            dev.close()
            time.sleep(.1)
            dev.open()
            continue
        if datalog_packet == b'':
            continue
        try:
            dl_packet = DatalogPacket(datalog_packet)
            dl_packet.parse_datalog(dl_chan_info.channels)
            datalog[time.asctime()] = dl_packet.datalog_dict
            log_file.write(str(dl_packet.datalog_dict))
            log_file.write('\n')
            log_file.flush()
        except:
            continue
    input("finished")