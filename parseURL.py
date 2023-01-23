import urllib3

supportedSites = ["sektedoujin.lol", "dojing.net"]
http = urllib3.PoolManager()

def parseURL(url):
    req = http.request('GET', url)
    
    if req.status == 200:
        pass
    else:
        print("Http Error")

    siteNum = supChecker(url)
    return req.data, siteNum

def parseOnly(url):
    req = http.request('GET', url)

    if req.status == 200:
        pass
    else:
        print("Http Error")

    return req.data

def supChecker(url):
    siteNo :int = 1
    for link in supportedSites:
        chk = url.find(link)
        if chk > 0:
            return siteNo
        else:
            siteNo += 1
