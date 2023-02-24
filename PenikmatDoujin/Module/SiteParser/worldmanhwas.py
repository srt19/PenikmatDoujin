from bs4 import BeautifulSoup

nameExc = ['<title>', '</title>', ':', '<', '>', '/', '*', '\\', '|', '\"']

def extractTitle(content, ch_type, ch_number):
    try:
        parsedHTML = BeautifulSoup(content, 'html.parser')
        rawTitle = parsedHTML.find('div', id='manga-title')
        for i in rawTitle.find_all('span'):
            i.decompose()
        for title in rawTitle.find("h1"):
            tt = title.text
            tt = tt.strip()
            seriesTitle = tt
        for name in nameExc:
            seriesTitle = seriesTitle.replace(name, '')
            
        rawCH = parsedHTML.find('div', id='chapterlist')
        chapterTitle = []

        ch = parsedHTML.find('ul', class_='main')
        for i in ch.find_all('a'):
            name = i.text
            name = name.strip()
            chapterTitle.append(name)
        chapterTitle.reverse()

        chName = []
        if ch_type == "comma":
            for i in ch_number:
                chName.append(chapterTitle[i - 1])

        elif ch_type == "dash":
            for i in range(ch_number[0] - 1, ch_number[1]):
                chName.append(chapterTitle[i])

        elif ch_type == "single":
            chName = chapterTitle[ch_number - 1]

        else:
            chName = chapterTitle

    except Exception as e:
        print(f"Error Occured: {e}")
        raise SystemExit(0)
    
    return seriesTitle, chName
