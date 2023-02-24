from os.path import basename
from urllib3 import PoolManager
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import shutil

supportedSites = ["sektedoujin.lol", "dojing.net", "kumapoi.me", "qinimg.com", "komiklokal", "worldmanhwas.info"]
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

def parseCh(content, ch_type, ch_number, siteNum):
    parsedHTML = BeautifulSoup(content, 'html.parser')
    rawLink = []
    chLink = []

    if siteNum != 5:
        parsedHTML = parsedHTML.find("div", id="chapterlist")
        for link in parsedHTML.find_all(class_="dt"):
            link.decompose()
        for link in parsedHTML.find_all('a'):
            rawLink.append(link.get('href'))
        rawLink.reverse()
    
    else:
        ch = parsedHTML.find('ul', class_='main')
        for i in ch.find_all('a'):
            rawLink.append(i.get('href'))
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

def parseIMG(content, siteNum):
    parsedIMG = []
    fileName = []
    parsedHTML = BeautifulSoup(content, 'html.parser')

    if siteNum == 5:
        parsedHTML = parsedHTML.find('div', class_='reading-content')
        for i in parsedHTML.find_all('img'):
            link = i.get('src')
            link = link.strip()
            parsedIMG.append(link)

    else:
        parsedHTML = parsedHTML.find('div', id='readerarea')
        for link in parsedHTML.find_all('img'):
            parsedIMG.append(str(link.get('src')))

    for link in parsedIMG:
        rawName = urlparse(link)
        name = str(basename(rawName.path))
        fileName.append(name)
    
    if len(parsedIMG) == 0:
        parsedIMG, fileName = parseLazy(content)

    return parsedIMG, fileName

def parseLazy(content):
    parsedHTML = BeautifulSoup(content, 'html.parser')
    parsedHTML = parsedHTML.find_all('script')
    for i in parsedHTML:
        if "ts_reader" in str(i):
            raw = str(i)
    a = raw.find("images")
    b = raw.find("lazyload")
    clean = raw[a+9:b-5]
    clean = clean.replace('"', '')
    clean = clean.replace("\/", '/')
    parsedIMG = clean.split(',')
    fileName = []
    for i,n in zip(range(1, len(parsedIMG)+1), parsedIMG):
        if "jpg" in n:
            fileName.append(str(i).zfill(2)+".jpg")
        elif "png" in n:
            fileName.append(str(i).zfill(2)+".png")
    
    return parsedIMG, fileName
