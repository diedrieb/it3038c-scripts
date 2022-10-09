const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    total_memory=os.totalmem();
    free_memory=os.freemem();
    uptime_seconds=os.uptime();
    uptime_minutes=uptime_seconds/60;
    uptime_hours=uptime_minutes/60;
    uptime_days=uptime_hours/24;
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${uptime_days + "Day(s)" + uptime_hours + "Hour(s)" + uptime_minutes + "Minute(s)" + uptime_seconds + "Second(s)"}</p>
        <p>Total Memory: ${total_memory / (1024 * 1024) + "MB"}</p>
        <p>Free Memory: ${free_memory / (1024 * 1024) + "MB"}</p>
        <p>Number of CPUs: ${os.cpus().length}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");
