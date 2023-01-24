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
            for name in nameExc:
                chapterTitle = chapterTitle.replace(name, '')

        except Exception as e:
            print(f"Error Occured: {e}")
            return
    
    return seriesTitle, chapterTitle
