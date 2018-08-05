from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
 
class SimpleEcho(WebSocket):
 
    def handleMessage(self):
        # echo message back to client
        print(self.data)
        
        # unicodeで送信しないとエラーがでる
        self.sendMessage(u"ok")
 
 
    def handleConnected(self):
        print(self.address, 'connected')
 
    def handleClose(self):
        print(self.address, 'closed')
 
server = SimpleWebSocketServer('', 8080, SimpleEcho)
server.serveforever()

