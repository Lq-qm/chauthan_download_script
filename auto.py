import os
import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://chauthanh.info/animeost/browse/A.html")

# Lista Geral
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letra = input("coloque a letra desejada: ")
if letra in letras:
    posicao = letras.index(letra) + 2
    print("letra selecionada: " + letra)
# Listagem dos links das letras
    lista = driver.find_element_by_xpath('//*[@id="content"]/p/a[%s]' % (posicao))
    link_letra = lista.get_attribute("href")
    print(link_letra)
# Listagem dos albums de acordo com a letra escolhida
    driver.get(link_letra)
    with open('links.txt', 'w') as arquivo:
        for contagem in range(1, 10000):
            try:
                lista_letra = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/span[%s]/a' % (contagem))
                link_album = lista_letra.get_attribute('href')
                arquivo.write(link_album + '\n')
            except Exception as e:
                album = input(str("qual album voce quer? "))
                os.system("grep -w" + album + "links.txt")
                break     
    captura_link_album = input("cole o link do album: ")
# Listagem das Musicas do Album Escolhido
    driver.get(captura_link_album)
    for contagem in range(1, 10000):
        try:
            driver.get(link_album)
            lista_album = driver.find_element_by_xpath('//*[@id="content"]/div[2]/table/tbody/tr[%s]/td[1]/a' % (contagem))
            link_musica = lista_album.get_attribute('href')
            driver.get(link_musica)
            download_musica = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/p/a[1]')
            link_download_musica = download_musica.get_attribute('href')
            print(link_download_musica)
            arquivo.write(link_download_musica + "\n") # Salvando o link da musica
            driver.get(link_album)
        except Exception as e:
            print("links salvos em" + album + ".txt ")
            driver.close()
            break
else:
    print("letra invalida")