import os
from bs4 import BeautifulSoup
from dl import dlIMG
from tqdm.contrib.concurrent import process_map
from urllib.parse import urlparse

nameExc = ['<title>', '</title>', ':', '<', '>', '/', '*', '\\', '|', '\"', " - Bahasa Indonesia"]
cpuCount = int(os.cpu_count()) - 1

def extractTitle(content, multi):
    parsedHTML = BeautifulSoup(content, 'html.parser')

    if multi == True:
        try:
            for title in parsedHTML.find_all(id='titlemove'):
                seriesTitle = title.text
                seriesTitle = seriesTitle.replace("\n", "")
            for name in nameExc:
                seriesTitle = seriesTitle.replace(name, '')
            rawCH = parsedHTML.find('div', id='chapterlist')
            chapterTitle = []
            for name in rawCH.find_all(class_='chapternum'):
                chapterTitle.append(name.text)
            chapterTitle.reverse()

        except Exception as e:
            print(f"Error Occured: {e}")
            return
        
    else:
        try:
            tt = parsedHTML.find(class_='allc')
            for title in tt.find_all('a'):
                seriesTitle = title.text
            title = str(parsedHTML.title)
            for name in nameExc:
                seriesTitle = seriesTitle.replace(name, '')
            remNum = title.find('Chapter')
            chapterTitle = title[remNum:]
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
    for link in parsedHTML.find_all('a'):
        chLink.append(link.get('href'))

    chLink.reverse()
    
    return chLink