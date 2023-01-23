import os

site = ['SekteDoujin', 'Dojing']
rootDir = str(os.getcwd())
dlDir = f"{rootDir}\\Downloads"

def checkDLFolder():
    if os.path.exists(dlDir) == False:
        os.mkdir(dlDir)

def siteFolder(num):
    if num == 1:
        siteDir = f"{dlDir}\\{site[0]}"
    elif num == 2:
        siteDir = f"{dlDir}\\{site[1]}"

    if os.path.exists(siteDir) == False:
        os.mkdir(siteDir)

    return siteDir

def seriesFolder(siteDir, seriesTitle):
    seriesDir = f"{siteDir}\\{seriesTitle}"
    if os.path.exists(seriesDir) == False:
        os.mkdir(seriesDir)
    
    return seriesDir

def chapFolder(seriesDir, chap):
    chapDir = f"{seriesDir}\\{chap}"
    if os.path.exists(chapDir) == False:
        os.mkdir(chapDir)
    return chapDir