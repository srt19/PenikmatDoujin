import argparse
import urllib3
import os
from parseURL import parseURL, parseOnly
import checkfolder

def main():
    # Write Arguments Here
    parMSG = "PenikmatDoujin | Manga Downloader"
    parser = argparse.ArgumentParser(description=parMSG)
    parser.add_argument("-l", "--link", required=True,
                        help="Input url here")
    parser.add_argument("-m", "--multi", action="store_true",
                        help="Download multi chapter at once")
    parser.add_argument("-c", "--compress", action="store_true",
                        help="Compress downloaded chapter to cbz")
    argL = parser.parse_args()

    checkfolder.checkDLFolder()
    content, siteNum = parseURL(argL.link)
    siteDir = checkfolder.siteFolder(siteNum)
    
    
    if siteNum == 1:
        from SiteParser import sektedoujin
        seriesTitle, chapterTitle = sektedoujin.extractTitle(content, argL.multi)
        seriesDir = checkfolder.seriesFolder(siteDir, seriesTitle)

        if argL.multi == True:
            chLink = sektedoujin.parseMulti(content)
            print(f"{seriesTitle} {len(chapterTitle)} Chapter/s")
            for link, chapter in zip(chLink, chapterTitle):
                chapterDir = checkfolder.chapFolder(seriesDir, chapter)
                content = parseOnly(link)
                os.chdir(chapterDir)
                sektedoujin.parseSingle(content, chapter)
                
                if argL.compress == True:
                    from compress import toCBZ
                    from shutil import rmtree
                    os.chdir(seriesDir)
                    toCBZ(chapter, chapterDir)
                    rmtree(chapterDir)
                    

        else:
            chapterDir = checkfolder.chapFolder(seriesDir, chapterTitle)
            os.chdir(chapterDir)
            print(f"{seriesTitle} 1 Chapter")
            sektedoujin.parseSingle(content, chapterTitle)

            if argL.compress == True:
                from compress import toCBZ
                from shutil import rmtree
                os.chdir(seriesDir)
                toCBZ(chapterTitle, chapterDir)
                rmtree(chapterDir)

    elif siteNum == 2:
        from SiteParser import dojing
        seriesTitle, chapterTitle = dojing.extractTitle(content, argL.multi)
        seriesDir = checkfolder.seriesFolder(siteDir, seriesTitle)
        
        if argL.multi == True:
            chLink = dojing.parseMulti(content)
            print(f"{seriesTitle} {len(chapterTitle)} Chapter/s")
            for link, chapter in zip(chLink, chapterTitle):
                chapterDir = checkfolder.chapFolder(seriesDir, chapter)
                content = parseOnly(link)
                os.chdir(chapterDir)
                dojing.parseSingle(content, chapter)
                
                if argL.compress == True:
                    from compress import toCBZ
                    from shutil import rmtree
                    os.chdir(seriesDir)
                    toCBZ(chapter, chapterDir)
                    rmtree(chapterDir)

        else:
            chapterDir = checkfolder.chapFolder(seriesDir, chapterTitle)
            os.chdir(chapterDir)
            print(f"{seriesTitle} 1 Chapter")
            dojing.parseSingle(content, chapterTitle)

            if argL.compress == True:
                from compress import toCBZ
                from shutil import rmtree
                os.chdir(seriesDir)
                toCBZ(chapterTitle, chapterDir)
                rmtree(chapterDir)

    else:
        print("Site Not Supported")

if __name__ == "__main__":
    main()