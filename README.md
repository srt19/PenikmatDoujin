# PenikmatDoujin

PenikmatDoujin is a software to download doujin from various site.
Currently only support download a single chapter or all chapter from supported site.

## What This Software Do

- ⬇️ Download image from supported site
- 🗜️ Compress downloaded image to cbz file
- 🗄️ Download all chapter from supported site

## How To Use

- First, clone this repository, and download all of requirements.

```python
git clone https://github.com/srt19/PenikmatDoujin.git
cd PenikmatDoujin
pip install -r Requirements.txt
```

- Input link from supported site with the option flags
- For single chapter

```python
python main.py -l "input link"
```

- For multi chapter

```python
python main.py -l "input link" -m
```

## Option Flags

| Option Flag | Description |
| :-: | :-: |
| -h / --help | Show help message |
| -l / --link url | Input url |
| -m / --multi | Download all chapter |
| -c / --compress | Compress downloaded image to cbz|

## Supported Site

| Site | URL |
| :-: | :-: |
| **SekteDoujin** | <https://sektedoujin.lol/>|
| **Dojing** | <https://dojing.net/> |
| **Mirrordesu** ✳️ | <https://mirrordesu.me/> |
| **Mareceh** ✳️ | <https://mareceh.com/> |
| **Kuma Poi** ✳️ | <https://kumapoi.me/> |
| **Komik Dewasa** ✳️ | <https://komiklokal.art/> |

✳️ : In development
