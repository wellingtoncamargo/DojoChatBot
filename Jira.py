# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

op = Options()
op.headless = True
driver = Chrome()
driver.implicitly_wait(60)
_url = 'https://jira.gft.com/secure/RapidBoard.jspa?rapidView=3167&view=detail&selectedIssue=FLEGUIAS-1'
# _url = 'https://idp.gft.com/cas-idp/login?service=https%3A%2F%2Fidp.gft.com%2Fidp%2FAuthn%2FRemoteUser%3Fconversation%3De1s1'
_btnCreate = (By.ID,'create_link')
_issueType = (By.ID,'issuetype-field')
_summary = (By.ID,'summary')

_story = (By.ID,'story-17')
_bug = (By.ID,'bug-18')
_improvement = (By.ID,'improvement-19')
_epic = (By.ID,'epic-20')
_task = (By.ID,'task-35')

_issueType2 = (By.CLASS_NAME, 'aui-icon icon-required')
# _issueType = (By.CLASS_NAME, 'icon aui-ss-icon noloading drop-menu')
driver.get(_url)


def click_in(id):
    driver.find_element(*id).click()


def escreva_in(id, txt):
    driver.find_element(*id).clear()
    sleep(1)
    driver.find_element(*id).send_keys(txt)


def alert():
    # driver.find_element_by_id("add_button").click()

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.dismiss()
        print("alert Negado")
    except TimeoutException:
        print("no alert")

def acao(Keys=None):
    actions = ActionChains(driver)
    actions.send_keys(Keys * 2)
    actions.perform()
    print('Passou')

# sleep(20)
# driver.switch_to.alert.send_keys(keys.TAB)
# driver.execute()

# acao(Keys.TAB)
# print(driver.get_cookies())
click_in(_btnCreate)

escreva_in(_issueType, 'Task')
sleep(3)
click_in(_issueType2)
escreva_in(_summary, 'Teste')
