from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os
from webdriver_manager.chrome import ChromeDriverManager


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(options=chrome_options)

    return driver


driver = iniciar_driver()
# ir até o site
driver.get('https://www.olx.com.br/computadores-e-acessorios/estado-sp/grande-campinas/regiao-de-campinas?q=computador%20regiao%20de%20campinas')

sleep(25)
#carregar todos elementos da tele movendo ate o final da tela e depois ate o topo
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(5)
driver.execute_script('window.scrollTo(0,document.body.scrollTop);')
sleep(5)
#encontrar os titulos
titulos = driver.find_element(By.XPATH,"//div[@class='sc-12rk7z2-7 kDVQFY']//h2")

#encontrar os valores
precos = driver.find_element(By.XPATH,"//span[@class='m7nrfa-0 eJCbzj sc-ifAKCX jViSDP']")

#encontrar os links ]
links = driver.find_element(By.XPATH,"//a[@data-lurker-detail='list_id']")

#guardar em um arquivo csv

for titulo, preco, link in zip(titulos, precos, links):
    with open('precos.csv', 'a' ,encoding='utf-8',newline='') as arquivo:
        link_processado = link.get_attribute('href')
        arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}')


input('')

driver.close()