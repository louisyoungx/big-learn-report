import os, json
from Log import log
from http.server import BaseHTTPRequestHandler

# Document https://docs.python.org/3.9/library/http.server.html

# 返回码
class ErrorCode(object):
    OK = "HTTP/1.1 200 OK\r\n"
    NOT_FOUND = "HTTP/1.1 404 Not Found\r\n"

# Content类型
class ContentType(object):
    HTML = 'Content-Type: text/html\r\n'
    CSS = "Content-Type: text/css\r\n"
    JavaScript = "Content-Type: application/javascript\r\n"
    PNG = 'Content-Type: img/png\r\n'

class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 处理一个GET请求
    def do_GET(self):
        self.rootDir = os.getcwd() + "/Static"
        url = self.requestline[4:-9]
        if (url == "/"):
            self.home()
        elif ("/api" in url):
            self.api(url[4:])
        else:
            self.file(url)

    def home(self):

        file_path = self.rootDir + "/index.html"
        home_page_file = open(file_path, 'r')
        content = str(home_page_file.read())
        
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content.encode())

    def file(self, url):
        Page = '''\
            <html>
            <body>
            <p>{}</p>
            </body>
            </html>
        '''
        content = str(log.get_data())
        content = Page.format(content)
        
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content.encode())

    def api(self, url):
        # ----------------------------------------------------------------
        # 此处写API
        
        if (url == "/log"):
            content = str(log.get_data())
        else:
            content = "No Response"


        # ----------------------------------------------------------------
        jsondict = {}
        jsondict["data"] = content
        res = json.dumps(jsondict)
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(res)))
        self.end_headers()
        self.wfile.write(res.encode())

    def nofound(self):
        pass
        