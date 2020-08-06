import json
import pprint

from requests import get
from selenium.webdriver.common.by import By
from conversas import conv
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep

op = Options()
op.headless = True
driver = Chrome(options=op)
driver.implicitly_wait(20)

driver.get('https://www.btgpactualdigital.com/fundos-de-investimento/arx-income-fia')
sleep(15)
_json = dict()
for a in driver.find_elements_by_class_name('mdc-layout-grid__cell--span-1-desktop'):
    try:
        ab = a.text.split('\n')
        if ab[1] != '-':
            _json.setdefault(ab[0], ab[1])
        else:
            pass

    except IndexError:
        pass

print(_json)


driver.close()
driver.quit()
