from ClassData.DataAPI import ClassInfoData, nameFormatter, ClassExistsList
from Message import send_group_message


def DataAPI():
    name = "18081102洪静"
    classID = "180816"
    classMemList = ClassInfoData(classID)
    id_name = nameFormatter(name, classMemList)
    print(id_name)

def sendGroupMes():
    remindMes = '''180811班共25人
已完成17人，未完成8人

未完成
2021-06-23
18081110-丁雨
18081113-曾泓康
18081126-王子通
18081128-辛旭晖
18081130-杨思达
18081132-韩秉昊
18081133-李桐
18081136-王世豪
'''
    classGroupID = {
        '180811': "114885461",
        '180812': "734448313",
        '180813': "1102498439",
        '180814': "249636458",
        '180815': "784723743",
        '180816': "",
        '180831': "",
        '180832': "",
        '180841': "769014619",
        '180842': "870609384",
        '180851': "787052100",
        '180852': "689574801",
    }
    #for classID in classExistsList:
    groupID = 114885461
    send_group_message(remindMes, groupID)

if __name__ == '__main__':
    sendGroupMes()