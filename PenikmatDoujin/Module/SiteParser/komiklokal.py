from bs4 import BeautifulSoup

nameExc = ['<title>', '</title>', ':', '<', '>', '/', '*', '\\', '|', '\"', " - Bahasa Indonesia"]

def extractTitle(content, ch_type, ch_number):
    try:
        parsedHTML = BeautifulSoup(content, 'html.parser')
        for title in parsedHTML.find_all(class_='entry-title'):
            seriesTitle = title.text
        for name in nameExc:
            seriesTitle = seriesTitle.replace(name, '')
        rawCH = parsedHTML.find('div', id='chapterlist')
        chapterTitle = []

        for name in rawCH.find_all(class_='chapternum'):
            chapterTitle.append(name.text)
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
