from urllib3 import PoolManager
from multiprocessing.pool import ThreadPool

http = PoolManager()

def dlIMG(link, fname):
    try:
        r = http.request('GET', link)
        with open(fname, 'wb') as f:
            f.write(r.data)

    except Exception as e:
        print("Error Occured")
        print(e)
        return