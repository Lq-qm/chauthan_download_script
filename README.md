# chauthan_download_script
Script in python to download musics from Chauthan using Jdownloader2

## What is Chauthan?

Chauthan is a website to download OST's from Animes and Games. 
You can download music for free but you can only download one music per time. 
If you have a premium account, you can download a zipped file of an album. This Script literally gives you a premium download routine.

# Disclaimer:

**I dont't encourage piracy! The website is free to download music and this script is just a quality of life improvement. If you liked Chauthan work, consider to donate to the website.**

## Requiriments:

* Python3.11
* Selenium 4.2.0
* Chromewebdriver
* Webdrivermanager
* Google Chrome
* Jdownloader2

## How it works:

The **"lista_chau.py"** is a script to list all album url's from a choosed letter and write them to a .txt file called "links_.txt".
The **"download_chau.py"** is the script that picks all download links of an album url and write them all to a .txt file called "musicas.txt".
Them you just copy all the links writed on "musicas.txt" with the Jdownloader2 running.

**In fact, you just need the "download_chau.py" to list all download links from an album url. The "lista_chau.py" script is just if you don't want to access the browser directly. ;)**

## How to Prepare your Python Enviromnent:

You can use a Python package manager like pyenv, conda (miniconda) or just install the python packages directly to python base enviromnent.

## To install:

```
pip install selenium==4.2.0
```
```
pip install chromewebdriver
```
```
pip install webdrivermanager
```

You will need **google chrome** installed too for Selenium to work.

After you prepared you enviromnent, you will need **Jdownloader2**, a download manager that can download a list of links at the same time.

## How to use it:

### If you want to just copy/paste an album link:

Just execute the "download_chau.py" script from your terminal 

```
python3 download_chau.py
```

It will ask for you **username and password** from the website forum. After that it will ask for the Link of the album.
The script will write all download links to a .txt file called "musicas.txt".
Just open the "musicas.txt" and copy everything with Jdownloader2 running and Voula!

### If you want to use the "lista_chau.py" script:

On your terminal:

```
python3 lista_chau.py
```

It will list all album links from a selected Letter directly on your terminal. If you are on windows, you can just copy/paste, if you are or linux, you can use the grep function. After that, just use the "download_chau.py" script as mencioned above.
