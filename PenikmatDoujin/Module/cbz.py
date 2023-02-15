import zipfile
import pathlib

def toCBZ(chapter, chapterDir):
    rDir = pathlib.Path(chapterDir)
    print(f"Compressing {chapter}")
    try:
        with zipfile.ZipFile(f"{chapter}.cbz", mode='w') as arc:
            for fpath in rDir.iterdir():
                arc.write(fpath, arcname=fpath.name)
    
    except Exception as e:
        print(f"Error Occured: {e}")