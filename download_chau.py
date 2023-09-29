import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
link_album = input("link do album: ")

# Listagem das Musicas do Album Escolhido
with open("musicas.txt", "w") as arquivo:
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
            print("links salvos em musicas.txt ")
            driver.close()
            break