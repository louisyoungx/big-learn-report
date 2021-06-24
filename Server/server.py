import json
from http.server import HTTPServer
from Log import log
from Server.requestHandler import RequestHandler
from Settings import LOCAL_HOST, PORT, SERVER_HOST, DEBUG

def server():
    if DEBUG == True:
        name = LOCAL_HOST
    else:
        name = SERVER_HOST
    port = PORT
    host = LOCAL_HOST
    serverAddress = (host, port)
    log.update("(Server): http://{}:{}/".format(name, port))
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
