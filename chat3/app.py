import sys
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

f = open("./index.html");
content = f.read()
f.close()

def app(environ, start_response):
    if environ["PATH_INFO"] == '/echo':
        ws = environ["wsgi.websocket"]
        while True:
            src = ws.receive()
            if src is None:
                break
            ws.send(rb,src)
    else:
        start_response("200 OK", [
                ("Content-Type", "text/html"),
                ("Content-Length", str(len(content)))
                ])  
        return iter([content])

if __name__=="__main__":
    server = pywsgi.WSGIServer(('127.0.0.1', 8000), app, handler_class=WebSocketHandler)
    server.serve_forever()