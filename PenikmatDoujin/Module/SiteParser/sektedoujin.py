from bs4 import BeautifulSoup

nameExc = ['<title>', '</title>', ':', '<', '>', '/', '*', '\\', '|', '\"', " - Bahasa Indonesia"]

def extractTitle(content, multi, chapterNumber):
    parsedHTML = BeautifulSoup(content, 'html.parser')

    if multi == True:
        try:
            for title in parsedHTML.find_all(class_='entry-title'):
                seriesTitle = title.text
            for name in nameExc:
                seriesTitle = seriesTitle.replace(name, '')
            rawCH = parsedHTML.find('div', id='chapterlist')
            chapterTitle = []

            for name in rawCH.find_all(class_='chapternum'):
                chapterTitle.append(name.text)
            chapterTitle.reverse()
            chName = list()
            if chapterNumber != None:
                for x in chapterNumber:
                    chName.append(chapterTitle[x - 1])
            else:
                chName = chapterTitle

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
    
    return seriesTitle, chName
