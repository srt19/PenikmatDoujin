import urllib3, os
from bs4 import BeautifulSoup
from urllib.parse import urlparse

supportedSites = ["sektedoujin.lol", "dojing.net", "mirrordesu.me", "qinimg.com", "mareceh.com", "kumapoi.me", "komiklokal.art"]
http = urllib3.PoolManager()

def supportChecker(url):
    siteNo :int = 1
    for link in supportedSites:
        chk = url.find(link)
        if chk > 0:
            return siteNo
        else:
            siteNo += 1

def parseLink(url):
    req = http.request('GET', url)
    
    if req.status == 200:
        pass
    else:
        print("Http Error")

    siteNum = supportChecker(url)
    return req.data, siteNum

def parseOnly(url):
    req = http.request('GET', url)

    if req.status == 200:
        pass
    else:
        print("Http Error")

    return req.data

def parseSingle(content):
    parsedHTML = BeautifulSoup(content, 'html.parser')
    parsedHTML = parsedHTML.find('div', id='readerarea')
    parsedIMG = []
    fileName = []
    for link in parsedHTML.find_all('img'):
        parsedIMG.append(str(link.get('src')))

    for link in parsedIMG:
        rawName = urlparse(link)
        name = str(os.path.basename(rawName.path))
        fileName.append(name)

    return parsedIMG, fileName

def parseMulti(content, siteNum):
    chLink = []
    parsedHTML = BeautifulSoup(content, 'html.parser')
    parsedHTML = parsedHTML.find(id='chapterlist')

    for link in parsedHTML.find_all(class_='dt'):
        link.decompose()
    for link in parsedHTML.find_all('a'):
        chLink.append(link.get('href'))

    chLink.reverse()

    return chLink

def parseQinMulti(content):
    titleLink = []
    parsedHTML = BeautifulSoup(content, 'html.parser')
    parsedHTML = parsedHTML.find(class_='list_box')
    for link in parsedHTML.find_all('a'):
        link = link.get('href')
        link = "https://www.qinimg.com" + link
        titleLink.append(link)
    del titleLink[-1]
    
    return titleLink


def parseQinSingle(content):
    parsedIMG = []
    fileName = []
    parsedHTML = BeautifulSoup(content, 'html.parser')
    parsedHTML = parsedHTML.find(class_='img_box')
    for link in parsedHTML.find_all('a'):
        parsedIMG.append(link.get('href'))
    for link in parsedIMG:
        rawName = urlparse(link)
        name = str(os.path.basename(rawName.path))
        fileName.append(name)

    return parsedIMG, fileName