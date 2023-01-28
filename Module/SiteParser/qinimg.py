import urllib3
from bs4 import BeautifulSoup

nameExc = ['<title>', '</title>', ':', '<', '>', '/', '*', '\\', '|', '\"', " Qinimg", "  "]

def extractTitle(content, multi):
    parsedHTML = BeautifulSoup(content, 'html.parser')

    if multi == True:
        try:
            seriesTitle = []
            rt = parsedHTML.find(class_='list_box')
            for title in rt.find_all('a'):
                seriesTitle.append(title.get('title'))
            del seriesTitle[-1]

        except Exception as e:
            print(f"Error Occured: {e}")
            return
        
    else:
        try:
            seriesTitle = str(parsedHTML.title)
            for x in nameExc:
                seriesTitle = seriesTitle.replace(x, '')

        except Exception as e:
            print(f"Error Occured: {e}")
            return
    
    return seriesTitle