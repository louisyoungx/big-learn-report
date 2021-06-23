import csv
file_name = "2018-class-name.csv"
with open(file_name, 'r', encoding="utf-8") as RawText:
    reader = csv.reader(RawText)
    fieldnames = next(reader)#获取数据的第一列，作为后续要转为字典的键名 生成器，next方法获取
    print(fieldnames)
    csv_reader = csv.DictReader(RawText, fieldnames=fieldnames)
    totalList = []
    existClass = []
    for item in csv_reader:
        ID = item["ID"]
        Name = item["Name"]
        ClassID = item["ClassID"]

        if ClassID not in existClass:
            thisDict = {
                "ClassID": ClassID,
                "MemberList": []
            }
            totalList.append(thisDict)
            existClass.append(ClassID)
        else:
            for ClassItem in totalList:
                if ClassItem["ClassID"] == ClassID:
                    ClassItem["MemberList"].append("{}-{}".format(ID, Name))

print(totalList)
print(existClass)

TotalList = [
    {
        "ClassID": 180851,
        "MemberList": [
            "18085132-刘洋兴",
        ]
    },
        {
        "ClassID": 180852,
        "MemberList": [
            "18085132-刘洋兴",
        ]
    }
]