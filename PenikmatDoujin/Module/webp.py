import os
from pathlib import Path
from PIL import Image
from tqdm import tqdm

def WEBP(chapter, chapterDir):
    bar = '{l_bar}{bar} | {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
    imgl = []
    for f in Path(chapterDir).rglob('*.jpg'):
        imgl.append(f)
    for f in Path(chapterDir).rglob('*.png'):
        imgl.append(f)
        
    try:
        for i in tqdm(imgl, desc=f"Converting {chapter}", colour="blue", bar_format=bar):
            a = str(i)
            Convert_WEBP(a)
    except Exception as e:
        print(f"Error Occured: {e}")
        raise SystemExit(0)

def Convert_WEBP(file):
    out = file[:-3]
    out = out + "webp"
    with Image.open(file) as img:
        img.save(out, quality=75)
    size1 = os.path.getsize(file)
    size2 = os.path.getsize(out)
    if size1 > size2:
        os.remove(file)
    else:
        os.remove(out)