from selenium.webdriver.common.by import By
from conversas import conv
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep


class BotWeb():

    def __init__(self):
        op = Options()
        op.headless = True
        self.driver = Chrome(options=op)
        self.driver.implicitly_wait(15)
        self.respostas = (By.CLASS_NAME,'WAC__bot-message')
        self.pergunta = (By.CLASS_NAME,'WAC__TextArea-textarea')
        self.btn = (By.ID,'WAC__send-button')
        self.WaitText = (By.CLASS_NAME, 'WAC__RichText')
        self.retorno = 'Did you mean:'
        self.retorno2 = 'Ainda não fui treinado para falar sobre esse assunto...'
        # self._url = 'https://web-chat.global.assistant.watson.cloud.ibm.com/preview.html?region=us-south&integrationID=d124b8aa-0744-44e5-9719-3c8675cc9403&serviceInstanceID=ae4691d0-deef-4df0-8b2f-666db7d5d7d6'
        self._url = 'https://bityli.com/KzdTC'

    def arquivoOK(self,text, resp):
        _conv = open('conversas_Ok.txt', 'a', encoding='utf-8')
        _conv.writelines(f"pergunta: {text},\n resposta: {resp}\n\n")
        _conv.close()

    def arquivo_Erro(self,text, resp):
        _conv = open('conversas_com_Erro.txt', 'a', encoding='utf-8')
        _conv.writelines(f"pergunta: {text},\n resposta: {resp}\n\n")
        _conv.close()

    def bot(self):
        self.driver.get(self._url)
        for per in conv:
            self.driver.find_element(*self.pergunta).send_keys(per)
            sleep(1)
            self.driver.find_element(*self.btn).click()
            sleep(3)
            teste = list(self.driver.find_elements(*self.WaitText))
            frase = teste[-2].text
            if frase != self.retorno and frase != self.retorno2:
                self.arquivoOK(per, frase)
                print(per)
                print(frase)
                print('===' * 50)
            else:
                self.arquivo_Erro(per, frase)
                print(per)
                print(frase)
                print('===' * 50)
        self.driver.close()
        self.driver.quit()


BotWeb().bot()
