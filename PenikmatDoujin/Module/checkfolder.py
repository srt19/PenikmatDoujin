import os

site = ['SekteDoujin', 'Dojing', 'KumaPoi', 'QinImg', 'KomikLokal', 'WorldManhwas', 'FastManhwa']
rootDir = str(os.getcwd())
if os.name == "nt":
    slash = "\\"
elif os.name == "posix":
    slash = "/"
else:
    print("You got a really weird OS")
    raise SystemExit(0)

dlDir = f"{rootDir}{slash}PenikmatDoujin"

def checkDLFolder():
    if os.path.exists(dlDir) == False:
        os.mkdir(dlDir)

def siteFolder(num):
    siteDir = f"{dlDir}{slash}{site[num]}"

    if os.path.exists(siteDir) == False:
        os.mkdir(siteDir)

    return siteDir

def seriesFolder(siteDir, seriesTitle):
    seriesDir = f"{siteDir}{slash}{seriesTitle}"
    if os.path.exists(seriesDir) == False:
        os.mkdir(seriesDir)
    
    return seriesDir

def chapFolder(seriesDir, chap):
    chapDir = f"{seriesDir}{slash}{chap}"
    if os.path.exists(chapDir) == False:
        os.mkdir(chapDir)
    chk = os.listdir(chapDir)

    if len(chk) > 0:
        print("There's already existing file in chapter folder")
        
        while True:
            asn = input("Type (Y)es to continue or (N) to abort\n")
            if asn.lower() in ['y', 'yes']:
                pass
                break

            elif asn.lower() in ['n', 'no']:
                print("Aborting")
                raise SystemExit(0)
    
    return chapDir