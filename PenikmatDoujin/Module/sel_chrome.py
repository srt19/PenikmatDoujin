from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from urllib3 import PoolManager
import os
from bs4 import BeautifulSoup

def lazy_load(url):
    driver_path = os.environ.get("ChromeDriver")
    if driver_path is None:
        print("ChromeDriver not found")
        raise SystemExit(0)

    ser = Service(executable_path=driver_path)

    options = Options()
    options.headless = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--disable-logging')
    options.add_argument('--log-level=3')
    options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
    )
    driver = webdriver.Chrome(service=ser, options=options)
    driver.get(url)
    content = driver.page_source
    driver.quit()
    
    return content

def parse(content):
    parsedHTML = BeautifulSoup(content, 'html.parser')
    parsedHTML = parsedHTML.find("div", id="readerarea")
    
    imgLink = []
    for link in parsedHTML.find_all("img"):
        imgLink.append(link.get("data-src"))

    return imgLink