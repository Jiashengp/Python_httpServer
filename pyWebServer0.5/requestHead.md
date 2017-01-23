waiting for a connection
# request resource is HTML DOM
GET / HTTP/1.1
Host: localhost:8200
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8
If-None-Match: W/"269-1482321927478"

# request resource is css
waiting for a connection
GET /style.css HTTP/1.1
Host: localhost:8200
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Accept: text/css,*/*;q=0.1
Referer: http://localhost:8200/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8
If-None-Match: W/"269-1482321927478"

# request resource is javascript
waiting for a connection
GET /script.js HTTP/1.1
Host: localhost:8200
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
If-None-Match: W/"269-1482321927478"
Accept: */*
Referer: http://localhost:8200/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8

#Content-Type: text/html;charset=utf-8
