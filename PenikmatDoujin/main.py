import os, shutil
from argparse import ArgumentParser
from tqdm.contrib.concurrent import process_map
from .Module.parseURL import *
from .Module import checkfolder
from .Module.dl import dlIMG
from .Module.chnumber import total_chapter

def main():
    # Write Arguments Here
    pdVer = "V1.1"
    parMSG = f"PenikmatDoujin {pdVer} | Doujin Downloader"
    parser = ArgumentParser(description=parMSG)
    parser.add_argument("-c", "--chapter", default=None, type=str, metavar="Ch Number",
                        help="Select Chapter Number to Download. ex: 1,4,7 or 1-5.")
    parser.add_argument("-cbz", action="store_true",
                        help="Compress downloaded chapter to cbz.")
    parser.add_argument("-webp", action='store_true',
                        help="Convert downloaded image to webp.")
    parser.add_argument("-t", "--thread", default='4', type=int, metavar="Number of threads",
                        help="Set download thread, default is 4.")
    parser.add_argument("-l", "--link", metavar="URL", required=True,
                        help="Input url here.")
    argL = parser.parse_args()

    thread = argL.thread
    content, siteNum = parseLink(argL.link)
    checkfolder.checkDLFolder()
    siteDir = checkfolder.siteFolder(siteNum)
    ch_number, ch_type = total_chapter(argL.chapter)
    bar = '{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
    width = shutil.get_terminal_size().columns
    
    # WIP 
    if siteNum == 0:
        from .Module.SiteParser import sektedoujin
        seriesTitle, chapterTitle = sektedoujin.extractTitle(content, ch_type, ch_number)

    elif siteNum == 1:
        from .Module.SiteParser import dojing
        seriesTitle, chapterTitle = dojing.extractTitle(content, ch_type, ch_number)
    
    elif siteNum == 2:
        from .Module.SiteParser import mirrordesu
        seriesTitle, chapterTitle = mirrordesu.extractTitle(content, argL.multi)
    
    elif siteNum == 3:
        from .Module.SiteParser import qinimg
        seriesTitle = qinimg.extractTitle(content, argL.multi)

    else:
        print("Site Not Supported".center(width))
        raise SystemExit(0)

    if siteNum != 4:
        seriesDir = checkfolder.seriesFolder(siteDir, seriesTitle)

        if ch_type == "all":
            ch_number = len(chapterTitle)
            chLink = parseCh(content, ch_type, ch_number)
            print(f"{seriesTitle} {len(chapterTitle)} Chapters".center(width))
            for link, chapter in zip(chLink, chapterTitle):
                chapterDir = checkfolder.chapFolder(seriesDir, chapter)
                os.chdir(chapterDir)
                content = parseOnly(link)
                parsedIMG, fileName = parseIMG(content)
                dl = process_map(dlIMG, parsedIMG, fileName, desc=chapter,
                                    colour='blue', bar_format=bar, max_workers=thread)

                if argL.webp == True:
                    from .Module.webp import WEBP
                    WEBP(chapter, chapterDir)

                if argL.cbz == True:
                    from .Module.cbz import toCBZ
                    from shutil import rmtree

                    os.chdir(seriesDir)
                    toCBZ(chapter, chapterDir)
                    rmtree(chapterDir)
        
        elif ch_type == "single":
            chapterDir = checkfolder.chapFolder(seriesDir, chapterTitle)
            os.chdir(chapterDir)
            print(f"{seriesTitle} Chapter {ch_number}".center(width))
            link = parseCh(content, ch_type, ch_number)
            content = parseOnly(link)
            parsedIMG, fileName = parseIMG(content)
            dl = process_map(dlIMG, parsedIMG, fileName, desc=chapterTitle,
                                colour='blue', bar_format=bar, max_workers=thread)
            
            if argL.webp == True:
                    from .Module.webp import WEBP
                    WEBP(chapterTitle, chapterDir)

            if argL.cbz == True:
                from .Module.cbz import toCBZ
                from shutil import rmtree

                os.chdir(seriesDir)
                toCBZ(chapterTitle, chapterDir)
                rmtree(chapterDir)
        
        elif ch_type == "comma":
            chLink = parseCh(content, ch_type, ch_number)
            print(f"{seriesTitle} {len(chapterTitle)} Chapters".center(width))
            for link, chapter in zip(chLink, chapterTitle):
                chapterDir = checkfolder.chapFolder(seriesDir, chapter)
                os.chdir(chapterDir)
                content = parseOnly(link)
                parsedIMG, fileName = parseIMG(content)
                dl = process_map(dlIMG, parsedIMG, fileName, desc=chapter,
                                    colour='blue', bar_format=bar, max_workers=thread)

                if argL.webp == True:
                    from .Module.webp import WEBP
                    WEBP(chapter, chapterDir)

                if argL.cbz == True:
                    from .Module.cbz import toCBZ
                    from shutil import rmtree

                    os.chdir(seriesDir)
                    toCBZ(chapter, chapterDir)
                    rmtree(chapterDir)

        elif ch_type == "dash":
            chLink = parseCh(content, ch_type, ch_number)
            chn = []
            for i in range(ch_number[0], ch_number[1]+1):
                chn.append(i)
            print(f"{seriesTitle} {len(chapterTitle)} Chapters".center(width))
            for link, chapter in zip(chLink, chapterTitle):
                chapterDir = checkfolder.chapFolder(seriesDir, chapter)
                os.chdir(chapterDir)
                content = parseOnly(link)
                parsedIMG, fileName = parseIMG(content)
                dl = process_map(dlIMG, parsedIMG, fileName, desc=chapter,
                                    colour='blue', bar_format=bar, max_workers=thread)

                if argL.webp == True:
                    from .Module.webp import WEBP
                    WEBP(chapter, chapterDir)

                if argL.cbz == True:
                    from .Module.cbz import toCBZ
                    from shutil import rmtree

                    os.chdir(seriesDir)
                    toCBZ(chapter, chapterDir)
                    rmtree(chapterDir)

if __name__ == "__main__":
    main()
