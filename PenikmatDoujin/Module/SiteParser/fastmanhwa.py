from bs4 import BeautifulSoup

nameExc = ['<title>', '</title>', ':', '<', '>', '/', '*', '\\', '|', '\"']

def extractTitle(content, ch_type, ch_number):
    try:
        parsedHTML = BeautifulSoup(content, 'html.parser')
        tt = parsedHTML.find('div', class_='post-title')
        for title in tt.find('h1'):
            seriesTitle = str(title).strip()
        for name in nameExc:
            seriesTitle = seriesTitle.replace(name, '')
        rawCH = parsedHTML.find('div', class_='c-page')
        chapterTitle = []

        for i in rawCH.find_all('span', class_='chapter-release-date'):
            i.decompose()

        for name in rawCH.find_all('a'):
            a = name.text
            chapterTitle.append(a.strip())

        del chapterTitle[0]
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
