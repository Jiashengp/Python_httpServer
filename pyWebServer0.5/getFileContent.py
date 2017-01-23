import sys
import os

def getHtmlFile(data):
    msgSendtoClient=""
    requestType=data[0:data.find("/")].rstrip()
    if requestType=="GET":
        msgSendtoClient=responseGetRequest(data,msgSendtoClient)
    if requestType=="POST":
        msgSendtoClient=responsePostRequest(data,msgSendtoClient)
    return msgSendtoClient

def getFile(msgSendtoClient,file):
        for line in file:
          msgSendtoClient+=line
        return msgSendtoClient

def getMidStr(data,startStr,endStr):
    startIndex = data.index(startStr)
    if startIndex>=0:
        startIndex += len(startStr)
        endIndex = data.index(endStr)
        return data[startIndex:endIndex]

def getFileSize(fileobject):
    fileobject.seek(0,2)
    size = fileobject.tell()
    return size

def setParaAndContext(msgSendtoClient,type,file,openFileType):
    msgSendtoClient+="Content-Type: "+type+";charset=utf-8"
    msgSendtoClient+="Content-Length: "+str(getFileSize(open(file,"r")))+"\n"+"\n"
    htmlFile=open(file,openFileType)
    msgSendtoClient=getFile(msgSendtoClient,htmlFile)
    return msgSendtoClient

def responseGetRequest(data,msgSendtoClient):
    return responseRequest(getMidStr(data,'GET /','HTTP/1.1'),msgSendtoClient)

def responsePostRequest(data,msgSendtoClient):
    return responseRequest(getMidStr(data,'POST /','HTTP/1.1'),msgSendtoClient)

def responseRequest(getRequestPath,msgSendtoClient):
    headFile=open("head.txt","r")
    msgSendtoClient=getFile(msgSendtoClient,headFile)
    if getRequestPath==" ":
        msgSendtoClient=setParaAndContext(msgSendtoClient,"text/html","index.html","r")
    else:
        rootPath=getRequestPath
        if os.path.exists(rootPath) and os.path.isfile(rootPath):
            if ".html" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"text/html",rootPath,"r")
            if ".css" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"text/css",rootPath,"r")
            if ".js" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"application/x-javascript",rootPath,"r")
            if ".gif" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"image/gif",rootPath,"rb")
            if ".doc" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"application/msword",rootPath,"rb")
            if ".mp4" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"video/mpeg4",rootPath,"rb")
        else:
            msgSendtoClient=setParaAndContext(msgSendtoClient,"application/x-javascript","file.js","r")
    return msgSendtoClient
