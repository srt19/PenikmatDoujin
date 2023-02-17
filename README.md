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
python main.py -c "Chapter Number" -l "input link"
```

- All Chapter

```python
python main.py -l "input link"
```

- Multi Chapter with Custom Range

```python
python main.py -c 1,4,7 or 1-5 -l "input url"
```

## Option Flags

| Option Flag | Description |
| :-: | :-: |
| -h / --help | Show help message |
| -l / --link url | Input url |
| -c | Select Chapter Number to Download. |
| -cbz | Compress downloaded image to cbz |
| -webp | Convert downloaded image to webp |

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
