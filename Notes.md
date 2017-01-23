## Notes:
#### 1. Create a Socket connection
```
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
```
#### 2. Bind IP&port
```
server_address = ('localhost', 8080)
sock.bind(server_address)
```
#### 3. Socket listen
```
sock.listen(1)
```
#### 4. Accept client rquest
```
connection, client_address = sock.accept()
```
#### 5. Get Client request data 
```
data = connection.recv(1024)
```
#### 6. Server response data to Client
```
connection.sendall(message)
```
When client is brower,if want to response data to get a static web,must to add Message header before Message entity.
#### 7. Close the connection
```
connection.close()
```
Formally,when server start up,we can't close the connection,always to monitor client request.

### Some need to take care
#### 1. When brower finined visit Server,then send a acquiescent request to Server(GET /favicon.ico HTTP/1.1)
#### 2. GET request usually to get resourse,POST usually to update resourse. And GET only commit 1024 byte data,but POST hava no limit
#### 3. For request head 
Content-Encoding: identity(compress) 
gzip or deflate will be error
#### 4. Count file size use seek(),tell()
```
file.seek(head,tail)
#Read file pointer location,0 is file head,2 is file tail,other is 1
file.tell()
#we can use seek() pointer move in file,and use tell() to record this process,So can get file size(bytes)
def getFileSize(fileobject):
    fileobject.seek(0,2)
    size = fileobject.tell()
    return size
#
```

