from enum import Enum

class priority_enum(Enum) :
    LOW  = "low",
    MEDIUM  = "medium",
    HIGH  = "high",
Priority  =  Enum('Priority', [('LOW',"low"), ('MEDIUM', "medium"), ('HIGH', "high")])
