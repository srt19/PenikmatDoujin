# PenikmatDoujin

[English](README.MD) | Indonesia

PenikmatDoujin merupakan software untuk mendownload dojin.

## Apa Yang Software Ini Bisa Lakukan

- ⬇️ Unduh gambar dari situs yg didukung
- ⬇️ Unduh chapter tertentu
- ⏬ Unduh semua chapter
- 🗜️ Kompres gambar yg sudah diunduh menjadi file cbz

## Cara Menggunakan

- Pertama, clone repositori ini dan unduh semua yang dibutuhkan.

```python
git clone https://github.com/srt19/PenikmatDoujin.git
cd PenikmatDoujin
pip install -r Requirements.txt
```

- Satu Chapter

```python
python main.py -l "input link"
```

- Semua Chapter

```python
python main.py -m -l "input link"
```

- Chapter Pilihan

```python
python main.py -m -n 1,4,7 or 1-5 -l "input url"
```

## Option Flags

| Option Flag | Deskripsi |
| :-: | :-: |
| -h / --help | Tampilkan bantuan |
| -l / --link url | Input url |
| -m / --multi | Unduh semua chapter. Tambahkan -n untuk memilih no chapter |
| -n | No chapter yg akan diunduh |
| -c / --compress | Kompres menjadi file cbz |

## Situs Yang Didukung

| Site | URL |
| :-: | :-: |
| **SekteDoujin** | <https://sektedoujin.lol/>|
| **Dojing** | <https://dojing.net/> |
| **QinIMG** | <https://www.qinimg.com/> |
| **Mirrordesu** ✳️ | <https://mirrordesu.me/> |
| **Mareceh** ✳️ | <https://mareceh.com/> |
| **Kuma Poi** ✳️ | <https://kumapoi.me/> |
| **Komik Dewasa** ✳️ | <https://komiklokal.art/> |

✳️ : Dalam Pengembangan
