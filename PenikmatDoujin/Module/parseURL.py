from os.path import basename
from urllib3 import PoolManager
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import shutil

supportedSites = ["sektedoujin.lol", "dojing.net", "mirrordesu.me", "qinimg.com", "mareceh.com", "kumapoi.me", "komiklokal.art"]
http = PoolManager()

def supportChecker(url):
    siteNo = 0
    for link in supportedSites:
        if link in url:
            return siteNo
        else:
            siteNo += 1


def parseLink(url):
    siteNum = supportChecker(url)
    if siteNum is None:
        print("Sites Not Supported".center(shutil.get_terminal_size().columns))
        raise SystemExit(0)
    
    req = http.request('GET', url)
    if req.status == 200:
        pass
    else:
        print("Http Error")

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
        name = str(basename(rawName.path))
        fileName.append(name)

    return parsedIMG, fileName

def parseMulti(content, chNum):
    chapterNum = chNumber(chNum)
    chLink = []
    parsedHTML = BeautifulSoup(content, 'html.parser')
    parsedHTML = parsedHTML.find(id='chapterlist')

    for link in parsedHTML.find_all(class_='dt'):
        link.decompose()
    for link in parsedHTML.find_all('a'):
        chLink.append(link.get('href'))

    chLink.reverse()
    chapterLink = list()
    if chNum != None:
        for n in chapterNum:
            chapterLink.append(chLink[n - 1])
    else:
        chapterLink = chLink

    return chapterLink

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
        name = str(basename(rawName.path))
        fileName.append(name)

    return parsedIMG, fileName

def parseCh(content, ch_type, ch_number):
    parsedHTML = BeautifulSoup(content, 'html.parser')
    parsedHTML = parsedHTML.find("div", id="chapterlist")
    rawLink = []
    chLink = []

    for link in parsedHTML.find_all(class_="dt"):
        link.decompose()
    for link in parsedHTML.find_all('a'):
        rawLink.append(link.get('href'))
    rawLink.reverse()

    if ch_type == "single":
        chLink = rawLink[ch_number - 1]

    elif ch_type == "comma":
        for i in ch_number:
            chLink.append(rawLink[i - 1])

    elif ch_type == "dash":
        for i in range(ch_number[0] - 1, ch_number[1]):
            chLink.append(rawLink[i])

    elif ch_type == "all":
        chLink = rawLink

    return chLink

def parseIMG(content):
    parsedHTML = BeautifulSoup(content, 'html.parser')
    parsedHTML = parsedHTML.find('div', id='readerarea')
    parsedIMG = []
    fileName = []
    for link in parsedHTML.find_all('img'):
        parsedIMG.append(str(link.get('src')))

    for link in parsedIMG:
        rawName = urlparse(link)
        name = str(basename(rawName.path))
        fileName.append(name)

    return parsedIMG, fileName