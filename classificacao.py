from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import json
import pprint
from time import sleep

# driver = webdriver.Chrome()
# driver.get('https://www.espn.com.br/futebol/classificacao/_/liga/BRA.1/ordenar/wins/dir/desce/temporada/2019')
# sleep(3)
op = Options()
op.headless = True
op.add_argument("--window-size=1920x1080")
op = Chrome(options=op)
op.get('https://br.advfn.com/bolsa-de-valores/bovespa/movida-on-MOVI3/cotacao')
op.add_cookie()

linhas = op.find_element_by_id('quote_top')
for Html_linha in linhas.find_elements_by_class_name('boxToolTip'):
    print(Html_linha)

op.close()
op.quit()

