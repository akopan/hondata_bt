from enum import Enum

from constants.channels import *


class ChannelSize(Enum):
    CS_BYTE = "Byte"
    CS_WORD = "Word"


class ChannelItemType(Enum):
    CT_BIT = "Bit"
    CT_NUMBER = "Num"
    CT_RPM = "Rpm"
    CT_SPEED = "Speed"
    CT_MBAR = "Press"
    CT_KPA = "Press"
    CT_TPS = "TPS"
    CT_INJ = "Inj"
    CT_IGN = "Ign"
    CT_RETARD = "Ign"
    CT_TEMP = "Temp"
    CT_PCT = "%"
    CT_PCT_SIGNED = "%"
    CT_5V = "Volt"
    CT_19V = "Volt"
    CT_LAMBDA = "Lam"
    default = "?"
    

# Channel Info
channel_info = {
    CID_RPM: "RPM",
    CID_Speed: "Speed",
    CID_Gear: "Gear",
    CID_MAP: "MAP",
    CID_MAPVoltage: "MAP voltage",
    CID_AFMVoltage: "AFM voltage",
    CID_AFMFlow: "AFM flow",
    CID_TPS: "TPS",
    CID_TPSVoltage: "TPS voltage",
    CID_ThrottlePlate: "Throttle plate",
    CID_Inj: "Injector duration",
    CID_InjPhase: "Injector phase",
    CID_Duty: "Injector duty",
    CID_Ign: "Ignition advance",
    CID_IgnDwell: "Ignition dwell",
    CID_IAT: "Intake air temperature",
    CID_ECT: "Coolant temperature",
    CID_ECT2: "Coolant temperature #2",
    CID_ECTCorrection: "IAT correction",
    CID_IATCorrection: "ECT correction",
    CID_PA: "Air pressure",
    CID_BatteryVoltage: "Battery",
    CID_VTS: "VTEC spool",
    CID_VTP: "VTEC pressure",
    CID_VTC_Cmd: "VTC command",
    CID_VTC_Actual: "VTC actual",
    CID_VTC_Duty: "VTC duty",
    CID_VTC_Phase: "VTC phase",
    CID_O2A_V: "O2A voltage",
    CID_O2A_C: "O2A current",
    CID_O2A_Heat: "O2A heater",
    CID_O2A_Heat_R: "O2A heater resistance",
    CID_O2B_V: "O2B voltage",
    CID_O2B_Heat: "O2B heater",
    CID_Lambda_Lambda: "Lambda",
    CID_Corr_Lambda: "Corrected lambda",
    CID_Target_Lambda: "Target lambda",
    CID_Wideband_V: "Wideband voltage",
    CID_Wideband_Lambda: "Wideband lambda",
    CID_ShortTermTrim: "Short term trim",
    CID_MedTermTrim: "Medium term trim",
    CID_LongTermTrim: "Long term trim",
    CID_ClosedLoopStatus: "Closed loop status",
    CID_KnockLevel: "Knock level",
    CID_KnockVoltage: "Knock voltage",
    CID_KnockThreshold: "Knock threshold",
    CID_KnockRetard: "Knock retard",
    CID_KnockLimit: "Knock ignition limit",
    CID_KnockControl: "Knock control",
    CID_KnockCount: "Knock count",
    CID_KnockCount1: "Knock #1",
    CID_KnockCount2: "Knock #2",
    CID_KnockCount3: "Knock #3",
    CID_KnockCount4: "Knock #4",
    CID_KnockCount5: "Knock #5",
    CID_KnockCount6: "Knock #6",
    CID_ACSwitch: "AC switch",
    CID_SCS: "Service connector",
    CID_BrakeSwitch: "Brake switch",
    CID_ClutchIn: "Clutch in",
    CID_PSP: "Power steering pressure",
    CID_ELD_Voltage: "Electrical load voltage",
    CID_ELD_Current: "Electrical load current",
    CID_ACClutch: "AC clutch",
    CID_CheckEngine: "Check engine",
    CID_FuelPump: "Fuel pump",
    CID_ReverseLock: "Reverse lock",
    CID_AltControl: "Alternator control",
    CID_IAB: "Secondary runners",
    CID_RadFan: "Radiator fan",
    CID_Datalogging: "Datalogging",
    CID_SecondaryTables: "Secondary tables",
    CID_RevLimiter: "Rev limiter",
    CID_IgnitionCut: "Ignition cut",
    CID_BoostCut: "Boost cut",
    CID_LaunchCut: "Launch cut",
    CID_LaunchRetard: "Launch retard",
    CID_ShiftCut: "Shift cut",
    CID_PurgeDuty: "Purge duty",
    CID_PurgeOpen: "Purge open",
    CID_BoostControl_Duty: "Boost control duty",
    CID_FTP: "Fuel tank pressure",
    CID_Nitrous1Arm: "Nitrous 1 arm",
    CID_Nitrous1On: "Nitrous 1 on",
    CID_Nitrous2Arm: "Nitrous 2 arm",
    CID_Nitrous2On: "Nitrous 2 on",
    CID_Nitrous3Arm: "Nitrous 3 arm",
    CID_Nitrous3On: "Nitrous 3 on",
    CID_AnalogInput1: "Analog 1",
    CID_AnalogInput2: "Analog 2",
    CID_AN0: "Analog input 0",
    CID_AN1: "Analog input 1",
    CID_AN2: "Analog input 2",
    CID_AN3: "Analog input 3",
    CID_AN4: "Analog input 4",
    CID_AN5: "Analog input 5",
    CID_AN6: "Analog input 6",
    CID_AN7: "Analog input 7",
    CID_DI0: "Digital input 0",
    CID_DI1: "Digital input 1",
    CID_DI2: "Digital input 2",
    CID_DI3: "Digital input 3",
    CID_DI4: "Digital input 4",
    CID_DI5: "Digital input 5",
    CID_DI6: "Digital input 6",
    CID_DI7: "Digital input 7",
    CID_TC_Speed_LF: "Traction control speed LF",
    CID_TC_Speed_RF: "Traction control speed RF",
    CID_TC_Speed_LR: "Traction control speed LR",
    CID_TC_Speed_RR: "Traction control speed RR",
    CID_TC_Slip: "Traction control slip",
    CID_TC_Turn: "Traction control turn",
    CID_TC_OverSlip: "Traction control over slip",
    CID_TC_Output: "Traction control output",
    CID_TC_Volts: "Traction control voltage",
    CID_TC_Retard: "Traction control retard",
    CID_TC_RevLimiter: "Traction control rev limiter",
    CID_FuelLevel: "Fuel level",
    CID_FuelEconomy: "Fuel economy",
    CID_FuelUsed: "Fuel used",
    CID_EthanolContent: "Ethanol content",
    CID_FuelTemp: "Fuel Temp",
    CID_ABS_Speed_LF: "ABS speed LF",
    CID_ABS_Speed_RF: "ABS speed RF",
    CID_ABS_Speed_LR: "ABS speed LR",
    CID_ABS_Speed_RR: "ABS speed RR",
    CID_SteeringAngle: "Steering angle",
    CID_SteeringTorque: "Steering torque",
    CID_BrakePressure: "Brake pressure",
    CID_ClutchPosition: "Clutch position",
    CID_GLat: "G latitude",
    CID_GLong: "G longitude",
    CID_YawRate: "Yaw rate"
}
