# PenikmatDoujin

English | [Indonesia](README.ID.MD)

PenikmatDoujin is a software to download doujin from various site.

## What This Software Do

- ⬇️ Download image from supported site
- ⬇️ Download custom range chapter
- ⏬ Download all chapter
- 🗜️ Compress downloaded image to cbz file

## How To Install

Make sure you've already install Python 3.7 or newer.
Then run this in commandline.

```python
pip install penikmatdoujin
```

## How To Use

- Input link from supported site with the option flags
- Single Chapter

```python
python main.py -l "input link"
```

- Multi Chapter

```python
python main.py -m -l "input link"
```

- Multi Chapter with Custom Range

```python
python main.py -m -n 1,4,7 or 1-5 -l "input url"
```

## Option Flags

| Option Flag | Description |
| :-: | :-: |
| -h / --help | Show help message |
| -l / --link url | Input url |
| -m / --multi | Download all chapter. Add -n flag to select chapter number |
| -n | Select Chapter Number to Download. |
| -c / --compress | Compress downloaded image to cbz |

## Supported Site

| Site | URL |
| :-: | :-: |
| **SekteDoujin** | <https://sektedoujin.lol/>|
| **Dojing** | <https://dojing.net/> |
| **QinIMG** | <https://www.qinimg.com/> |
| **Mirrordesu** ✳️ | <https://mirrordesu.me/> |
| **Mareceh** ✳️ | <https://mareceh.com/> |
| **Kuma Poi** ✳️ | <https://kumapoi.me/> |
| **Komik Dewasa** ✳️ | <https://komiklokal.art/> |

✳️ : In development
