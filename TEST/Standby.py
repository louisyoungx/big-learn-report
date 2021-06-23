import re
from django.http import HttpResponse
import json
from django.views import View
from Applications.ClassManager.AutoLogin.ClassJsonGet import AutoRequests
from Applications.ClassManager.AutoLogin.SeleniumJsonGet import AutoSelenium
from Applications.ClassManager.ClassData.Data import ClassMemberInfo


# Create your views here.



class DXXJsonView(View):
    def get(self,request):
        url = 'https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/branch-api/course/records?pageSize=20&pageNum=1&desc=createTime&nid=N001300081008&course=C0002&accessToken=7E355C99-87D6-4E5F-8257-DA6E5B795AF0'
        auto = AutoSelenium()
        jsonList = auto.Selenium("180851_102377", "466976")
        ClassMemberInfo_Reverse = {}
        for key, value in ClassMemberInfo.items():
            ClassMemberInfo_Reverse[value] = key
        MemberDict = {}
        MemberList = []
        ClassMemberInfo_Do = eval(str(ClassMemberInfo))
        for member in jsonList:
            name = member
            index = name

            if "-" in name:
                index = name[0:8]
                name = ClassMemberInfo.get(index)
            elif len(name) == 8:
                index = name
                name = ClassMemberInfo.get(index)
            elif len(name) < 4:
                index = ClassMemberInfo_Reverse.get(name)
                name = name
            elif len(name) > 8:
                if re.search(r'[1-9]', name[0]):
                    index = name[0:8]
                    name = ClassMemberInfo.get(index)
                else:
                    if re.search(r'[1-9]', name[2]):
                        name = name[0:2]
                        index = ClassMemberInfo_Reverse.get(name)
                    else:
                        name = name[0:3]
                        index = ClassMemberInfo_Reverse.get(name)
            else:
                if re.search(r'[1-9]', name[0]):
                    index = name[0:8]
                    name = ClassMemberInfo.get(index)
                else:
                    name = name[0:3]
                    index = ClassMemberInfo_Reverse.get(name)

            ClassMemberInfo_Do.pop(index)

            MemberDict["index"] = index
            MemberDict["name"] = name

            MemberList.append(eval(str(MemberDict)))

        NotDict = {}
        NotList = []
        for Mem in ClassMemberInfo_Do:
            NotDict["index"] = Mem
            NotDict["name"] = ClassMemberInfo_Do.get(Mem)
            NotList.append(eval(str(NotDict)))

        ReturnJson = {}
        ReturnJson["DoMember"] = MemberList
        ReturnJson["NotMember"] = NotList
        ReturnJson["AllNum"] = len(ClassMemberInfo)
        ReturnJson["DoNum"] = len(MemberList)
        ReturnJson["DontNum"] = len(NotList)


        jsonStr = json.dumps(ReturnJson)
        return HttpResponse(jsonStr)

    def post(self,request):
        pass