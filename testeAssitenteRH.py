from selenium.webdriver import Chrome
import requests
from bs4 import BeautifulSoup
import json
import http.client
import mimetypes
from conversas import conv
from conversas_com_Erro import perguntas_Erro as PE

def arquivo():
    conv = open('conversas.txt', 'r', encoding='utf-8')
    return conv.readlines()

def arquivo_Erro(text, resp):
    _conv = open('conversas_com_Erro.txt','a',encoding='utf-8')
    _conv.writelines(f"pergunta: {text},\n resposta: {resp}\n\n")
    _conv.close()

def arquivoOK(text, resp):
    _conv = open('conversas_Ok.txt', 'a', encoding='utf-8')
    _conv.writelines(f"pergunta: {text},\n resposta: {resp}\n\n")
    _conv.close()


def Watson(text):
    url = "https://assistant-chat-us-south.watsonplatform.net/public/message/d19fcfaa-95eb-4e0d-866d-5c9330dc66f9?version=2020-04-01"

    payload = "{\n    \"value\": {\n        \"input\": {\n            \"text\": \""+text+"\",\n            \"options\": {\n                \"export\": true,\n                \"debug\": true,\n                \"return_context\": true\n            }\n        },\n        \"context\": {\n            \"global\": {\n                \"system\": {\n                    \"timezone\": \"America/Sao_Paulo\"\n                }\n            },\n            \"skills\": {\n                \"main skill\": {\n                    \"system\": {\n                        \"state\": \"eyJzZXNzaW9uX2lkIjoiOTVjMWQwODQtMzJlYi00NGNiLWFlNzYtNmJmYWRmOWI3MzQ4Iiwic2tpbGxfcmVmZXJlbmNlIjoibWFpbiBza2lsbCIsImFzc2lzdGFudF9pZCI6IjNmYzY2Y2E2LWQyMjUtNGJiYS1hNGQ5LTEwN2I4OTA2MGYxYyIsImluaXRpYWxpemVkIjp0cnVlLCJkaWFsb2dfc3RhY2siOlt7ImRpYWxvZ19ub2RlIjoiRW0gb3V0cm9zIGNhc29zIn1dLCJfbm9kZV9vdXRwdXRfbWFwIjp7IkJlbS12aW5kbyI6eyIwIjpbMF19LCJub2RlXzdfMTU3OTIwMTE1MzgzMCI6eyIwIjpbMCwwLDIsMV19LCJFbSBvdXRyb3MgY2Fzb3MiOnsiMCI6WzBdfX0sImxhc3RfYnJhbmNoX25vZGUiOiJFbSBvdXRyb3MgY2Fzb3MifQ==\"\n                    },\n                    \"user_defined\": {\n                        \"clean\": \"{input:{\\\"text\\\":\\\"\\\"}}\"\n                    }\n                }\n            }\n        },\n        \"history\": {\n            \"timestamp\": 1588693505642\n        }\n    },\n    \"session_id\": \"95c1d084-32eb-44cb-ae76-6bfadf9b7348\",\n    \"user_id\": \"anonymous_IBMuid-c6647fae-aa20-4dc9-8d70-9ad453969bff\"\n}"
    headers = {
        'Accept': 'application/json',
        'X-Global-Transaction-ID': '8eecbbac-4db0-4b56-8a51-418a4147fc20',
        'authorization': 'undefined',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'DNT': '1',
        'x-watson-is-preview': 'true',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    generic = json.loads(response.text.encode('utf8'))
    try:
        resposta = generic['output']['generic'][0]['text']
        if resposta != None and resposta != 'Qual tipo de licença?' and resposta != 'Ainda estou sendo treinado para responder essa questão.... O que deseja fazer agora?':
            arquivoOK(text, resposta)
            return resposta

        elif resposta == 'Qual tipo de licença?':
            arquivo_Erro(text, 'Resposta "Qual tipo de licença?" está fora de contexto, realizar confirmação via web')

        elif resposta == 'Ainda estou sendo treinado para responder essa questão.... O que deseja fazer agora?':
            arquivo_Erro(text, 'Resposta "Ainda estou sendo treinado para responder essa questão.... O que deseja fazer agora?" precisa ser confirmada via web')

    except IndexError:
        arquivo_Erro(text, f'"{text}" não houve resposta!')
        return f'"{text}" não houve resposta!'
    except KeyError:
        cont = list(generic['output']['generic'][0]['suggestions']).__len__()
        res = set()

        for i in range(cont):
            value = generic['output']['generic'][0]['suggestions'][i]['output']['generic']
            if len(value) != 0:
                res.add(value[0]['text'])
                arquivoOK(text, res)
                return res
            else:
                arquivo_Erro(text,f'{text} em branco')






textos= ['NÃO BATI, O QUE FAÇO?']

for i in conv:
    print('Pergunta:',i)
    print('Resposta:',Watson(i))
    print('=====' * 50)

