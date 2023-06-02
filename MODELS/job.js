const http = require('http');
const socketIO = require('socket.io');

const server = http.createServer((req,res)=> {
    // handle http requests 
});

const io = socketIO(server);

io.on('connection', (socket) => {
    console.log('A client has connected.');
    // listeners
    socket.on('disconnect',() =>{
        console.log('A client has disconnected');
    });
});

const fs = require('fs');

server.on('request',(req,res) => {
    if(req.url === '/'){
        res.writeHead(200,{'Content-Type' : 'text/html'});
        res.end(fs.readFileSync('./trail.html'));
    }
});

const port = 5500;
server.listen(port, () => {
    console.log('Server is runnign on http://localhost:${port}');
});