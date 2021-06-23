import requests

def AutoRequests(url):
    User_Header = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = User_Header)
    r.encoding = r.apparent_encoding
    print('Encoding:'+r.encoding)
    print('Status Code:'+str(r.status_code))
    body = r.text

    with open("Request.json", "w") as f:
        f.write(body)

    return body

if __name__ == "__main__":
    url = 'https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/branch-api/course/records?pageSize=20&pageNum=1&desc=createTime&nid=N001300081008&course=C0002&accessToken=7E355C99-87D6-4E5F-8257-DA6E5B795AF0'
    body = AutoRequests(url)
    print(body)
