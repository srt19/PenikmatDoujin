import os, shutil
from argparse import ArgumentParser
from tqdm.contrib.concurrent import process_map
from .Module.parseURL import *
from .Module import checkfolder
from .Module.dl import dlIMG
from .Module.chnumber import total_chapter

def main():
    # Write Arguments Here
    pdVer = "V1.2a"
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
    qin_multi = False
    
    # Conditional site import
    if siteNum == 0:
        from .Module.SiteParser import sektedoujin
        seriesTitle, chapterTitle = sektedoujin.extractTitle(content, ch_type, ch_number)

    elif siteNum == 1:
        from .Module.SiteParser import dojing
        seriesTitle, chapterTitle = dojing.extractTitle(content, ch_type, ch_number)
    
    elif siteNum == 2:
        from .Module.SiteParser import kumapoi
        seriesTitle, chapterTitle = kumapoi.extractTitle(content, ch_type, ch_number)
    
    elif siteNum == 3:
        from .Module.SiteParser import qinimg
        if "tags" in argL.link:
            print("multi")
            qin_multi = True
        elif "images" in argL.link:
            print("single")
            qin_multi = False 
        seriesTitle = qinimg.extractTitle(content, qin_multi)
    
    elif siteNum == 4:
        from .Module.SiteParser import komiklokal
        seriesTitle, chapterTitle = komiklokal.extractTitle(content, ch_type, ch_number)

    elif siteNum == 5:
        from .Module.SiteParser import Manhwa18
        seriesTitle, chapterTitle = Manhwa18.extractTitle(content, ch_type, ch_number)

    else:
        print("Site Not Supported".center(width))
        raise SystemExit(0)
    
    # Since site4 or QinImg has no chapter
    if siteNum != 3:
        seriesDir = checkfolder.seriesFolder(siteDir, seriesTitle)

        if ch_type == "all":
            ch_number = len(chapterTitle)
            chLink = parseCh(content, ch_type, ch_number, siteNum)
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
            link = parseCh(content, ch_type, ch_number, siteNum)
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
            chLink = parseCh(content, ch_type, ch_number, siteNum)
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
            chLink = parseCh(content, ch_type, ch_number, siteNum)
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
    
    elif siteNum == 3:
        if qin_multi is True:
            print(f"Downloading {len(seriesTitle)} Title/s".center(width))
            titleLink = parseQinMulti(content)
            for name, link in zip(seriesTitle, titleLink):
                seriesDir = checkfolder.seriesFolder(siteDir, name)
                os.chdir(seriesDir)
                content = parseOnly(link)
                parsedIMG, fileName = parseQinSingle(content)
                dl = process_map(dlIMG, parsedIMG, fileName, desc=name,
                                colour='blue', bar_format=bar, max_workers=thread)
                if argL.webp == True:
                    from .Module.webp import WEBP
                    WEBP(name, seriesDir)
        else:
            print(f"Downloading {seriesTitle}".center(width))
            seriesDir = checkfolder.seriesFolder(siteDir, seriesTitle)
            os.chdir(seriesDir)
            parsedIMG, fileName = parseQinSingle(content)
            dl = process_map(dlIMG, parsedIMG, fileName, desc=seriesTitle,
                                colour='blue', bar_format=bar, max_workers=thread)
            if argL.webp == True:
                    from .Module.webp import WEBP
                    WEBP(seriesTitle, seriesDir)

if __name__ == "__main__":
    main()
