import os
from bs4 import BeautifulSoup
from dl import dlIMG
from tqdm.contrib.concurrent import process_map
from urllib.parse import urlparse

nameExc = ['<title>', '</title>', ':', '<', '>', '/', '*', '\\', '|', '\"', " - Bahasa Indonesia"]

def extractTitle(content, multi):
    parsedHTML = BeautifulSoup(content, 'html.parser')

    if multi == True:
        try:
            for title in parsedHTML.find_all(class_='entry-title'):
                seriesTitle = title.text
            seriesTitle = seriesTitle.replace("\n", "")
            rawCH = parsedHTML.find('div', id='chapterlist')
            chapterTitle = []
            for name in rawCH.find_all(class_='chapternum'):
                chapterTitle.append(name.text)
            for name in nameExc:
                seriesTitle = seriesTitle.replace(name, "")
            chapterTitle.reverse()

        except Exception as e:
            print(f"Error Occured: {e}")
            return
        
    else:
        try:
            tt = parsedHTML.find(class_='allc')
            for title in tt.find_all('a'):
                seriesTitle = title.text
            for name in nameExc:
                seriesTitle = seriesTitle.replace(name, '')
            ch = parsedHTML.find(class_='entry-title')
            chapterTitle = ch.text
        except Exception as e:
            print(f"Error Occured: {e}")
            return

    return seriesTitle, chapterTitle

def parseSingle(content, chapter):
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

    dl = process_map(dlIMG, parsedIMG, fileName, max_workers=4,
        desc=f"Downloading {chapter}", colour='blue', unit='file')

def parseMulti(content):
    parsedHTML = BeautifulSoup(content, 'html.parser')
    chLink = []
    parsedHTML = parsedHTML.find(id='chapterlist')
    for link in parsedHTML.find_all(class_='dt'):
        link.decompose()
    for link in parsedHTML.find_all('a'):
        chLink.append(link.get('href'))

    chLink.reverse()
    
    return chLink