from os.path import basename
from urllib3 import PoolManager
from bs4 import BeautifulSoup
from urllib.parse import urlparse

supportedSites = ["sektedoujin.lol", "dojing.net", "mirrordesu.me", "qinimg.com", "mareceh.com", "kumapoi.me", "komiklokal.art"]
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64'}
http = PoolManager(headers=user_agent)

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
        name = str(basename(rawName.path))
        fileName.append(name)

    return parsedIMG, fileName

def parseMulti(content, siteNum, chNum):
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

def chNumber(chNum):
    if chNum != None:
        try:
            if ',' in chNum:
                chpar = chNum.split(',')
                for x, n in zip(chpar, range(len(chpar))):
                    chpar[n] = int(x)
                return chpar

            elif '-' in chNum:
                chpar = chNum.split('-')
                chapterNum = list()
                for x in range(int(chpar[0]), int(chpar[1]) + 1):
                    chapterNum.append(x)
                return chapterNum

            else:
                return None

        except Exception as e:
            print(f"Error Occured: {e}")
            raise SystemExit(0)