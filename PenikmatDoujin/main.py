import os
from argparse import ArgumentParser
from tqdm.contrib.concurrent import process_map
from .Module import parseURL
from .Module import checkfolder
from .Module.dl import dlIMG

def main():
    # Write Arguments Here
    parMSG = "PenikmatDoujin | Manga Downloader"
    parser = ArgumentParser(description=parMSG)
    parser.add_argument("-m", "--multi", action='store_true',
                        help="Download multi chapter at once")
    parser.add_argument("-cbz", action="store_true",
                        help="Compress downloaded chapter to cbz")
    parser.add_argument("-t", "--thread", default='4', type=int, metavar="Number of threads",
                        help="Set download thread")
    parser.add_argument("-l", "--link", required=True, metavar="URL",
                        help="Input url here")
    parser.add_argument("-n", default=None, type=str, metavar="Chapter Number",
                        help="Select Chapter Number to Download. ex: 1,4,7 or 1-5")
    argL = parser.parse_args()

    thread = argL.thread
    if thread == 0:
        thread = os.cpu_count()
    checkfolder.checkDLFolder()
    content, siteNum = parseURL.parseLink(argL.link)
    siteDir = checkfolder.siteFolder(siteNum)
    chapterNumber = parseURL.chNumber(argL.n)
    
    # WIP 
    if siteNum == 1:
        from .Module.SiteParser import sektedoujin
        seriesTitle, chapterTitle = sektedoujin.extractTitle(content, argL.multi, chapterNumber)

    elif siteNum == 2:
        from .Module.SiteParser import dojing
        seriesTitle, chapterTitle = dojing.extractTitle(content, argL.multi, chapterNumber)
    
    elif siteNum == 3:
        from .Module.SiteParser import mirrordesu
        seriesTitle, chapterTitle = mirrordesu.extractTitle(content, argL.multi)
    
    elif siteNum == 4:
        from .Module.SiteParser import qinimg
        seriesTitle = qinimg.extractTitle(content, argL.multi)

    else:
        print("Site Not Supported")
        raise SystemExit(0)

    if siteNum != 4:
        seriesDir = checkfolder.seriesFolder(siteDir, seriesTitle)

    if argL.multi == True and siteNum != 4:
        chLink = parseURL.parseMulti(content, siteNum, argL.n)
        print(f"{seriesTitle} {len(chapterTitle)} Chapter/s")
        for link, chapter in zip(chLink, chapterTitle):
            chapterDir = checkfolder.chapFolder(seriesDir, chapter)
            content = parseURL.parseOnly(link)
            os.chdir(chapterDir)
            parsedIMG, fileName = parseURL.parseSingle(content)
            dl = process_map(dlIMG, parsedIMG, fileName, desc=f"Downloading {chapter}",
                             colour='blue', unit='file', max_workers=thread)

            if argL.cbz == True:
                from compress import toCBZ
                from shutil import rmtree

                os.chdir(seriesDir)
                toCBZ(chapter, chapterDir)
                rmtree(chapterDir)

    elif argL.multi == False and siteNum != 4:
        chapterDir = checkfolder.chapFolder(seriesDir, chapterTitle)
        os.chdir(chapterDir)
        print(f"{seriesTitle} 1 Chapter")
        parsedIMG, fileName = parseURL.parseSingle(content)
        dl = process_map(dlIMG, parsedIMG, fileName, desc=f"Downloading {chapterTitle}",
                             colour='blue', unit='file', max_workers=thread)

        if argL.cbz == True:
            from compress import toCBZ
            from shutil import rmtree

            os.chdir(seriesDir)
            toCBZ(chapter, chapterDir)
            rmtree(chapterDir)

    elif argL.multi == True and siteNum == 4:
        print(f"Downloading {len(seriesTitle)} Title/s")
        titleLink = parseURL.parseQinMulti(content)
        for name, link in zip(seriesTitle, titleLink):
            seriesDir = checkfolder.seriesFolder(siteDir, name)
            os.chdir(seriesDir)
            content = parseURL.parseOnly(link)
            parsedIMG, fileName = parseURL.parseQinSingle(content)
            dl = process_map(dlIMG, parsedIMG, fileName, desc=f"Downloading {name}",
                             colour='blue', unit='file', max_workers=thread)

    elif argL.multi == False and siteNum == 4:
        print(f"{seriesTitle}")
        seriesDir = checkfolder.seriesFolder(siteDir, seriesTitle)
        os.chdir(seriesDir)
        parsedIMG, fileName = parseURL.parseQinSingle(content)
        dl = process_map(dlIMG, parsedIMG, fileName, desc=f"Downloading {seriesTitle}",
                             colour='blue', unit='file', max_workers=thread)

if __name__ == "__main__":
    main()
