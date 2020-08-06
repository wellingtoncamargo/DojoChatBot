from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver.chrome.options import Options
from time import sleep

op = Options()
#op.headless = True
#op.set_headless()
driver = Chrome()
driver.implicitly_wait(15)
coo = driver.get_cookies()

_user = (By.ID, 'username')
_pass = (By.ID, 'password')
_Inicio = (By.CLASS_NAME, 'slds-truncate')
_btn = (By.ID, 'Login')
_url = 'https://login.salesforce.com/'
_url2 = 'https://na172.lightning.force.com/lightning/setup/SetupOneHome/home'
_usuario = 'wellington.camargo@gft.com'
_senha = '"Wellsc2914"'

driver.get(_url)
driver.find_element(*_user).send_keys(_usuario)
driver.find_element(*_pass).send_keys(_senha)
driver.find_element(*_btn).click()
texto = driver.find_element(*_Inicio).text
print(texto)
