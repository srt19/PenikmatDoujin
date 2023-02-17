# PenikmatDoujin

[English](README.MD) | Indonesia

PenikmatDoujin merupakan software untuk mendownload dojin.

## Apa Yang Software Ini Bisa Lakukan

- ⬇️ Unduh gambar dari situs yg didukung
- ⬇️ Unduh chapter tertentu
- ⏬ Unduh semua chapter
- 🗜️ Kompres gambar yg sudah diunduh menjadi file cbz
- 🖼️ Konversi format gambar menjadi webp

## Cara Install

Pastikan anda sudah menginstall Python 3.7 atau yg lebih baru.
Lalu jalankan perintah ini di commandline.

```python
pip install penikmatdoujin
```

## Cara Menggunakan

- Gambar yg terunduh tersimpan di folder PenikmatDoujin/"Nama Situs"/"Judul Doujin"

- Satu Chapter

```python
penikmatdoujin atau pd -c "Nomor Chapter" "input link"
```

- Semua Chapter

```python
penikmatdoujin atau pd -l "input link"
```

- Chapter Pilihan

```python
penikmatdoujin atau pd -c 1,4,7 atau 1-5 -l "input url"
```

## Option Flags

| Option Flag | Deskripsi |
| :-: | :-: |
| -h / --help | Tampilkan bantuan |
| -l / --link url | Input url |
| -c | No chapter yg akan diunduh |
| -cbz | Kompres menjadi file cbz |
| -webp | Ubah format gambar ke webp|

## Situs Yang Didukung

| Site | URL |
| :-: | :-: |
| **SekteDoujin** | <https://sektedoujin.lol/>|
| **Dojing** | <https://dojing.net/> |
| **QinIMG** | <https://www.qinimg.com/> |
| **Kuma Poi** | <https://kumapoi.me/> |
| **Komik Dewasa** | <https://komiklokal.art/> |
| **Manhwa18** | <https://manhwa18.cc/> |

✳️ : Dalam Pengembangan
