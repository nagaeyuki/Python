// var WebSocketServer = require('ws').Server;
// var http = require('http');
// var express = require('express');
// var app = express();

// app.use(express.static(__dirname + '/'));

// var server = http.createServer(app);
// var wss = new WebSocketServer({ server: server });

// //Websocket接続を保存しておく
// var connections = [];

// //接続時
// wss.on('connection', function (ws) {
//   //配列にWebSocket接続を保存
//   console.log('-- websocket connected --');
//   ws.on('message', function (message) {
//     wss.clients.forEach(function each(client) {
//       if (isSame(ws, client)) {
//         console.log('- skip sender -');
//       }
//       else {
//         client.send(message);
//       }
//     });
//   });
// });

// function isSame(ws1, ws2) {
//   // -- compare object --
//   return (ws1 === ws2);
// }


// server.listen(3000);

export function detect(req, res) {

var exec = require('child_process').exec;
  exec('python test.py "' + req.body.image + '"',
    function(err, stdout, stderr) {
      if (err) { console.log(err); }
      console.log(stdout);
      return res.status(201).json({"face": stdout});
    }
  );

}