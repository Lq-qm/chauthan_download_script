from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

account = input("Account: ")
password = input("Password: ")

driver.get("https://chauthanh.info/forum/login.html")
driver.find_element("id", "username").send_keys(account)
driver.find_element("id", "password").send_keys(password)
driver.find_element(by=By.XPATH, value="//input[@value='Login']").click()

link_album = input("link do album: ")

with open("musicas.txt", "w") as arquivo:
    for contagem in range(1, 10000):
        try:
            driver.get(link_album)
            lista_album = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[2]/table/tbody/tr[%s]/td[1]/a' % (contagem))
            link_musica = lista_album.get_attribute('href')
            driver.get(link_musica)
            download_musica = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div[2]/p/a[1]')
            link_download_musica = download_musica.get_attribute('href')
            print(link_download_musica)
            arquivo.write(link_download_musica + "\n") # Salvando o link da musica
            driver.get(link_album)
        except Exception as e:
            print("links salvos em musicas.txt ")
            driver.close()
            break