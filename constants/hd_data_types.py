from enum import Enum

# Channel sizes
# Highest two bits of type are used as the size; rest are the type

class ChannelSizeType(Enum):
    CS_MASK = 0xC0
    CT_MASK = 0x3F
    # = 0x00 spare (bit)
    CS_BIT = 0x40 # 8 bits (same as byte currently)
    CS_BYTE = 0x40 # 8 bits
    CS_WORD = 0x80 # 16 bits
    CS_DWORD = 0xC0 # 32 bits


class ChannelDataType(Enum):
    # Channel data types
    CT_UNKNOWN = 0x00
    CT_BIT = 0x01 # byte 0=off, 1=on
    CT_NUMBER = 0x02 # byte or word
    CT_RPM = 0x03 # word revs unit=r/min lsb=1
    CT_SPEED = 0x04 # word (lsb=0.01 unit=kph)
    CT_MBAR = 0x05 # word mbar pressure
    CT_KPA = 0x06 # byte kpa pressure
    CT_TPS = 0x07 # byte lsb=0.5% range -20 to 108%
    CT_INJ = 0x08 # word lsb=0.001 ms
    CT_IGN = 0x09 # also used for cam angle
    CT_RETARD = 0x0B # byte retard 0-64 lsb=0.25
    CT_TEMP = 0x10 # byte lsb=1 offset=0 unit=ºF
    CT_PCT = 0x11 # byte percentage 0 to +100 lsb=128/100
    CT_PCT_SIGNED = 0x12 # byte percentage -100 to +100 lsb=128/100
    CT_PCT_CHG = 0x13 # word percentage uint=% 0 to 655.35% lsb=0.01%
    CT_MASSFLOW = 0x16 # mg/s mass flow
    CT_5V = 0x18 # byte 0-5 volts
    CT_19V = 0x19 # byte range=6-18.8V lsb=0.05V unit=volts
    CT_LAMBDA = 0x1E #
    CT_BAR = 0x20 # word lsb=1 unit=bar
    CT_MM = 0x21 # wastegate distance unit=mm
    CT_GFORCE = 0x22 # word
    CT_SIGNED = 0x23 # byte or word signed
    CT_SIGNED100 = 0x24 # byte or word signed, fixed 2 dp


ch_data_convert = {
    ChannelDataType.CT_UNKNOWN: (lambda val: val),
    ChannelDataType.CT_BIT: (lambda val: 'on' if val else 'off'), # byte 0=off, 1=on
    ChannelDataType.CT_NUMBER: (lambda val: val), # byte or word
    ChannelDataType.CT_RPM: (lambda val: val/4), # word revs unit=r/min lsb=1
    ChannelDataType.CT_SPEED: (lambda val: val/100), # word (lsb=0.01 unit=kph)
    ChannelDataType.CT_MBAR: (lambda val: val/10), # word mbar pressure
    ChannelDataType.CT_KPA: (lambda val: val/2), # byte kpa pressure
    ChannelDataType.CT_TPS: (lambda val: (val/2)-10), # byte lsb=0.5% range -20 to 108%
    ChannelDataType.CT_INJ: (lambda val: val/1000), # word lsb=0.001 ms
    ChannelDataType.CT_IGN: (lambda val: (val-20)/2), # also used for cam angle
    ChannelDataType.CT_RETARD: (lambda val: val/2), # byte retard 0-64 lsb=0.25
    ChannelDataType.CT_TEMP: (lambda val: val), # byte lsb=1 offset=0 unit=ºF
    ChannelDataType.CT_PCT: (lambda val: val/2.56), # byte percentage 0 to +100 lsb=128/100
    ChannelDataType.CT_PCT_SIGNED: (lambda val: (val-128)/1.28), # byte percentage -100 to +100 lsb=128/100
    ChannelDataType.CT_PCT_CHG: (lambda val: val/100), # word percentage uint=% 0 to 655.35% lsb=0.01%
    ChannelDataType.CT_MASSFLOW: (lambda val: val), # mg/s mass flow
    ChannelDataType.CT_5V: (lambda val: (val*5.0)/256.0), # byte 0-5 volts
    ChannelDataType.CT_19V: (lambda val: (val/20)+6), # byte range=6-18.8V lsb=0.05V unit=volts
    ChannelDataType.CT_LAMBDA: (lambda val: val/32768.0), #
    ChannelDataType.CT_BAR: (lambda val: val), # word lsb=1 unit=bar
    ChannelDataType.CT_MM: (lambda val: val), # wastegate distance unit=mm
    ChannelDataType.CT_GFORCE: (lambda val: val), # word
    ChannelDataType.CT_SIGNED: (lambda val: val), # byte or word signed
    ChannelDataType.CT_SIGNED100: (lambda val: val), # byte or word signed, fixed 2 dp
}
