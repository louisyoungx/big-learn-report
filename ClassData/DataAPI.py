import copy
from ClassData.ClassData import classExistsList, classDataDict, classGroupID
from Logs.logs import log


def ClassExistsList():
    return copy.deepcopy(classExistsList)

def ClassInfoData(ClassID=None):
    if ClassID is None:
        return copy.deepcopy(classDataDict)
    else:
        for classItem in classDataDict:
            if classItem["ClassID"] == ClassID:
                return copy.deepcopy(classItem["MemberList"])
        return {}

def ClassGroupID(ClassID):
    if ClassID not in ClassExistsList():
        return False
    return int(classGroupID[ClassID])

def nameFormatter(name, classMemList):
    if (name.isdigit()): # 18012345 / 45
        ID_Name = _nameFormatter_with_ID(name, classMemList)
    elif (name.isalpha()): # 曾建雄
        ID_Name = _nameFormatter_with_name(name, classMemList)
    elif (name.isalnum()): # 18012345曾建雄 / 曾建雄18012345
        ID_Name = _nameFormatter_with_ID_name(name, classMemList)
    elif ("-" in name or " " in name or " " in name or "—" in name or "/" in name): # 18012345-曾建雄 / 18012345 曾建雄
        ID_Name = _nameFormatter_with_ID_bar_name(name, classMemList)
    else:
        log.update("DataAPI.nameFormatter", "Invalid Name -> {}".format(name), debug="WARNING")
        return ""
    return ID_Name

def _nameFormatter_with_ID(ID, classMemList):
    if (len(ID) == 2):
        for member in classMemList:
            if member[6:8] == ID:
                return member
    elif (len(ID) == 8):
        for member in classMemList:
            if member[:8] == ID:
                return member
    log.update("DataAPI.nameFormatter_ID", "Invalid Name -> {}".format(ID), debug="WARNING")
    return ID

def _nameFormatter_with_name(name, classMemList):
    for member in classMemList:
        if member[9:] == name:
            return member
    log.update("DataAPI.nameFormatter_Name", "Invalid Name -> {}".format(name), debug="WARNING")
    return name

def _nameFormatter_with_ID_name(id_name, classMemList):
    if (id_name[0].isdigit()):
        for member in classMemList:
            if member[:8] == id_name[:8]:
                return member
        log.update("DataAPI.nameFormatter_IDName", "Invalid Name -> {}".format(id_name), debug="WARNING")
    else:
        for member in classMemList:
            if member[:8] == id_name[-8:]:
                return member
        log.update("DataAPI.nameFormatter_NameID", "Invalid Name -> {}".format(id_name), debug="WARNING")

def _nameFormatter_with_ID_bar_name(id_bar_name, classMemList):
    if (id_bar_name[0].isdigit()):
        for member in classMemList:
            if member[:8] == id_bar_name[:8]:
                return member
        log.update("DataAPI.nameFormatter_ID-Name", "Invalid Name -> {}".format(id_bar_name), debug="WARNING")
    else:
        for member in classMemList:
            if member[:8] == id_bar_name[-8:]:
                return member
        log.update("DataAPI.nameFormatter_Name-ID", "Invalid Name -> {}".format(id_bar_name), debug="WARNING")
