from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.MD"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

Version = '1.1a'
Desc = "Doujin Downlaoder"
Long_Desc = "A doujin downloader"

setup(
    name="penikmatdoujin",
    version=Version,
    author="AriKu",
    author_email="noobhek@gmail.com",
    description=Desc,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=['PenikmatDoujin', 'PenikmatDoujin.Module', 'PenikmatDoujin.Module.SiteParser'],
    install_requires=['tqdm', 'urllib3', 'bs4'],
    keywords=['python', 'manga', 'manga-downloader'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts':['penikmatdoujin=PenikmatDoujin.main:main'],
        'console_scripts':['pd=PenikmatDoujin.main:main'],
    }
)