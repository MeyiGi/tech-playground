const http = require("http")
const os = require("os")

function getLocalIP() {
    const nets = os.networkInterfaces();
    for (const name of Object.keys(nets)) {
        for (const net of nets[name]) {
            if((net.family =="IPv4" || net.family === 4) && !net.internal) {
                return net.address
            } 
        }
    }
}

http.createServer((req, res) => {
    if (req, res) {
        res.writeHead(200, {"Content-Type": "application/json"});
        res.end(JSON.stringify({ip: getLocalIP(), data: new Date().toLocaleDateString()}));
    }
}).listen(3000, () => {
    console.log("Server running on http://localhost:3000")
})