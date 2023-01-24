import argparse
import urllib3
import os
import parseURL
import checkfolder
from dl import dlIMG
from tqdm.contrib.concurrent import process_map

def main():
    # Write Arguments Here
    parMSG = "PenikmatDoujin | Manga Downloader"
    parser = argparse.ArgumentParser(description=parMSG)
    parser.add_argument("-m", "--multi", action="store_true",
                        help="Download multi chapter at once")
    parser.add_argument("-c", "--compress", action="store_true",
                        help="Compress downloaded chapter to cbz")
    parser.add_argument("-t", "--thread", default='4', type=int,
                        help="Set download thread")
    parser.add_argument("-l", "--link", required=True,
                        help="Input url here")
    argL = parser.parse_args()

    thread = argL.thread
    if thread == 0:
        thread = os.cpu_count()
    checkfolder.checkDLFolder()
    content, siteNum = parseURL.parseLink(argL.link)
    siteDir = checkfolder.siteFolder(siteNum)
    
    # WIP 
    if siteNum == 1:
        from SiteParser import sektedoujin
        seriesTitle, chapterTitle = sektedoujin.extractTitle(content, argL.multi)

    elif siteNum == 2:
        from SiteParser import dojing
        seriesTitle, chapterTitle = dojing.extractTitle(content, argL.multi)

    else:
        print("Site Not Supported")
        raise SystemExit(0)

    seriesDir = checkfolder.seriesFolder(siteDir, seriesTitle)

    if argL.multi == True:
        chLink = parseURL.parseMulti(content, siteNum)
        print(f"{seriesTitle} {len(chapterTitle)} Chapter/s")
        for link, chapter in zip(chLink, chapterTitle):
            chapterDir = checkfolder.chapFolder(seriesDir, chapter)
            content = parseURL.parseOnly(link)
            os.chdir(chapterDir)
            parsedIMG, fileName = parseURL.parseSingle(content)
            dl = process_map(dlIMG, parsedIMG, fileName, desc=f"Downloading {chapter}",
                             colour='blue', unit='file', max_workers=thread)

            if argL.compress == True:
                from compress import toCBZ
                from shutil import rmtree

                os.chdir(seriesDir)
                toCBZ(chapter, chapterDir)
                rmtree(chapterDir)

    elif argL.multi == False:
        chapterDir = checkfolder.chapFolder(seriesDir, chapterTitle)
        os.chdir(chapterDir)
        print(f"{seriesTitle} 1 Chapter")
        parsedIMG, fileName = parseURL.parseSingle(content)
        dl = process_map(dlIMG, parsedIMG, fileName, desc=f"Downloading {chapterTitle}",
                             colour='blue', unit='file', max_workers=thread)

        if argL.compress == True:
            from compress import toCBZ
            from shutil import rmtree

            os.chdir(seriesDir)
            toCBZ(chapter, chapterDir)
            rmtree(chapterDir)

if __name__ == "__main__":
    main()
