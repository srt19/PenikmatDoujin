import requests
from urllib.parse import urlparse
from os import path
from multiprocessing.pool import ThreadPool

def dlIMG(link, fname):
    try:
        r = requests.get(link)
        with open(fname, 'wb') as f:
            f.write(r.content)

    except Exception as e:
        print("Error Occured")
        print(e)
        return