import urllib3
from bs4 import BeautifulSoup

nameExc = ['<title>', '</title>', ':', '<', '>', '/', '*', '\\', '|', '\"', " - Bahasa Indonesia"]

def extractTitle(content, multi):
    parsedHTML = BeautifulSoup(content, 'html.parser')

    if multi == True:
        try:
            for title in parsedHTML.find_all(class_='entry-title'):
                seriesTitle = title.text
            for name in nameExc:
                seriesTitle = seriesTitle.replace(name, '')
            rawCH = parsedHTML.find('div', id='chapterlist')
            chapterTitle = []

            for link in rawCH.find_all(class_='chapterdate'):
                link.decompose()
            for name in rawCH.find_all(class_='eph-num'):
                x = str(name.text)
                x = x.replace('\n', '')
                chapterTitle.append(x)

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
