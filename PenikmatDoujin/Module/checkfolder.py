import os

site = ['SekteDoujin', 'Dojing', 'MirrorDesu', 'QinImg']
rootDir = str(os.getcwd())
if os.name == "nt":
    slash = "\\"
elif os.name == "posix":
    slash = "/"
else:
    print("You got a weird OS")
    raise SystemExit(0)

dlDir = f"{rootDir}{slash}PenikmatDoujin"

def checkDLFolder():
    if os.path.exists(dlDir) == False:
        os.mkdir(dlDir)

def siteFolder(num):
    if num == 0:
        siteDir = f"{dlDir}{slash}{site[0]}"
    elif num == 2:
        siteDir = f"{dlDir}{slash}{site[1]}"
    elif num == 2:
        siteDir = f"{dlDir}{slash}{site[2]}"
    elif num == 3:
        siteDir = f"{dlDir}{slash}{site[3]}"

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
            if asn in ['y', 'Y', 'yes']:
                pass
                break

            elif asn in ['n', 'N', 'no']:
                print("Aborting")
                raise SystemExit(0)
                break
    
    return chapDir