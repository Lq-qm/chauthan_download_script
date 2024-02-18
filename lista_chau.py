import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://chauthanh.info/animeost/browse/A.html")

# Lista Geral
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letra = input("Choose a letter: ")
if letra in letras:
    posicao = letras.index(letra) + 2
    print("letra selecionada: " + letra)
# Listagem dos links das letras
    lista = driver.find_element_by_xpath('//*[@id="content"]/p/a[%s]' % (posicao))
    link_letra = lista.get_attribute("href")
    print(link_letra)
# Listagem dos albums de acordo com a letra escolhida
    driver.get(link_letra)
    with open('links_' + letra + '_.txt', 'w') as arquivo:
        for contagem in range(1, 10000):
            try:
                lista_letra = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/span[%s]/a' % (contagem))
                link_album = lista_letra.get_attribute('href')
                print(link_album)
                arquivo.write(link_album + '\n')
            except Exception as e:
                print('Saved on links_' + letra + '_.txt')
                driver.close()
                break 
else:
    print("Invalid Letter")