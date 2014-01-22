import re
import os

def mkdirs(folderPath):
    if os.path.exists(folderPath) or folderPath == '':
        return
    base, file = os.path.split(folderPath)
    mkdirs(base)
    if os.path.exists(folderPath) or folderPath == '':
        return
    os.mkdir(folderPath)
    
def writeFile(path,content):
    if os.path.exists(path):
        return
    base, file = os.path.split(path)
    mkdirs(base)
    f = open(path,"w")
    f.write(content)
    f.close()
    

import httplib


def getHttpContent(baseURL,url):
    conn = httplib.HTTPConnection(baseURL)
    conn.request("GET",url)
    response = conn.getresponse()
    data=response.read()
    return data


def mainFun():
    baseDir = "/home/duun/gitSpace/facebook/tornado/static"
    '''get urls'''
    myPatten = re.compile(r'src="([^"]*)"')
#     myPatten = re.compile(r'href="([^"]*)"')
    myFile = open("./static/main.html")
    fileContent = myFile.read()
    arr = myPatten.findall(fileContent)
    myFile.close()
    baseURL = "thecoastalcupboard.com"
    
    for url in arr:
        if not url.endswith("/"):
            data = getHttpContent(baseURL,url)
            print "write data to "+baseDir + url
            writeFile(baseDir + url,data)

def mainFunCss():
    baseDir = "/home/duun/gitSpace/facebook/tornado/static"
    '''get urls'''
    myPatten = re.compile(r'url\("([^"]*)"\)')
#     myFile = open("./static/main.html")
    myFile = open("./static/assets/styles/global.css")
    fileContent = myFile.read()
    arr = myPatten.findall(fileContent)
    myFile.close()
    baseURL = "thecoastalcupboard.com"
    for url in arr:
        url = url.replace(r"..",r"/assets")
        data = getHttpContent(baseURL,url)
        print "write data to "+baseDir + url
        writeFile(baseDir + url,data)
        
def mainFunJS():
    baseDir = "/home/duun/gitSpace/facebook/tornado/static"
    '''get urls'''
    myPatten = re.compile(r'\'src\', \'([^\']*)\'')
# home/duun/gitSpace/facebook/tornado/static/assets/javascript/global.js
    myFile = open("./static/assets/javascript/global.js")
    fileContent = myFile.read()
    arr = myPatten.findall(fileContent)
    myFile.close()
    baseURL = "thecoastalcupboard.com"
    for url in arr:
        data = getHttpContent(baseURL,url)
        print "get from "+baseURL + url
        print "write data to "+baseDir + url
        writeFile(baseDir + url,data)

mainFunJS()
        
