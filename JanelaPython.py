import PySimpleGUI as pg
# from testeAssistenteRH_WEB import BotWeb
import requests
import json
import array
import pprint

class Tela:
    def __init__(self):
        #Layout
        layout = [
            [pg.Output(size=(50, 20))],
            [pg.Input(size=(45,3), key='texto', do_not_clear=False), pg.Button('Enviar')],
            # [pg.Text('Idade:', size=(6,0)), pg.Input(size=(40,0), key='idade')],
            # [pg.Text('Qual seu servidor de email?')],
            # [pg.Checkbox('Gmail', key='gmail'),pg.Checkbox('Outlook', key='outlook')],
            # [pg.Text('Aceita Cartão?')],
            # [pg.Radio('Sim', 'cartoes', key='s_card'),pg.Radio('Não', 'cartoes', key='n_card')],
            # [pg.Button('Enviar')]

        ]

        #Janela
        self.janela = pg.Window('Dados do Usuario').layout(layout)
        # self.Bot = BotWeb()

    # def watson(self, text = None):
    #     url = "https://assistant-chat-us-south.watsonplatform.net/public/message/d19fcfaa-95eb-4e0d-866d-5c9330dc66f9?version=2020-04-01"
    #
    #     payload = "{\n    \"value\": {\n        \"input\": {\n            \"text\": \"" + text + "\",\n            \"options\": {\n                \"export\": true,\n                \"debug\": true,\n                \"return_context\": true\n            }\n        },\n        \"context\": {\n            \"global\": {\n                \"system\": {\n                    \"timezone\": \"America/Sao_Paulo\"\n                }\n            },\n            \"skills\": {\n                \"main skill\": {\n                    \"system\": {\n                        \"state\": \"eyJzZXNzaW9uX2lkIjoiOTVjMWQwODQtMzJlYi00NGNiLWFlNzYtNmJmYWRmOWI3MzQ4Iiwic2tpbGxfcmVmZXJlbmNlIjoibWFpbiBza2lsbCIsImFzc2lzdGFudF9pZCI6IjNmYzY2Y2E2LWQyMjUtNGJiYS1hNGQ5LTEwN2I4OTA2MGYxYyIsImluaXRpYWxpemVkIjp0cnVlLCJkaWFsb2dfc3RhY2siOlt7ImRpYWxvZ19ub2RlIjoiRW0gb3V0cm9zIGNhc29zIn1dLCJfbm9kZV9vdXRwdXRfbWFwIjp7IkJlbS12aW5kbyI6eyIwIjpbMF19LCJub2RlXzdfMTU3OTIwMTE1MzgzMCI6eyIwIjpbMCwwLDIsMV19LCJFbSBvdXRyb3MgY2Fzb3MiOnsiMCI6WzBdfX0sImxhc3RfYnJhbmNoX25vZGUiOiJFbSBvdXRyb3MgY2Fzb3MifQ==\"\n                    },\n                    \"user_defined\": {\n                        \"clean\": \"{input:{\\\"text\\\":\\\"\\\"}}\"\n                    }\n                }\n            }\n        },\n        \"history\": {\n            \"timestamp\": 1588693505642\n        }\n    },\n    \"session_id\": \"95c1d084-32eb-44cb-ae76-6bfadf9b7348\",\n    \"user_id\": \"anonymous_IBMuid-c6647fae-aa20-4dc9-8d70-9ad453969bff\"\n}"
    #     headers = {
    #         'Accept': 'application/json',
    #         'X-Global-Transaction-ID': '8eecbbac-4db0-4b56-8a51-418a4147fc20',
    #         'authorization': 'undefined',
    #         'Content-Type': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    #         'DNT': '1',
    #         'x-watson-is-preview': 'true',
    #         'Content-Type': 'application/json'
    #     }
    #
    #     response = requests.request("POST", url, headers=headers, data=payload)
    #
    #     generic = json.loads(response.text.encode('utf8'))
    #     try:
    #         resposta = generic['output']['generic'][0]['text']
    #         if resposta != None and resposta != 'Qual tipo de licença?' and resposta != 'Ainda estou sendo treinado para responder essa questão.... O que deseja fazer agora?':
    #             return resposta
    #
    #         elif resposta == 'Qual tipo de licença?':
    #             return 'Resposta "Qual tipo de licença?" está fora de contexto, realizar confirmação via web'
    #
    #         elif resposta == 'Ainda estou sendo treinado para responder essa questão.... O que deseja fazer agora?':
    #             return 'Resposta "Ainda estou sendo treinado para responder essa questão.... O que deseja fazer agora?" precisa ser confirmada via web'
    #
    #         else:
    #             pass
    #     except IndexError:
    #         return f'"{text}" não houve resposta!'
    #     except KeyError:
    #         cont = list(generic['output']['generic'][0]['suggestions']).__len__()
    #         res = set()
    #
    #         for i in range(cont):
    #             value = generic['output']['generic'][0]['suggestions'][i]['output']['generic']
    #             if len(value) != 0:
    #                 res.add(value[0]['text'])
    #                 return res
    #             else:
    #                 return f'{text} em branco'

    def Iniciar(self):
        while True:
            # Extração de dados
            self.button, self.values = self.janela.Read()
            key = self.values
            texto = key['texto']
            # chat = self.Bot.bot(per=texto)
            # idade = key['idade']
            # gmail = key['gmail']
            # outlook = key['outlook']
            # s_card = key['s_card']
            # n_card = key['n_card']

            print('Você:',texto)
            # print('Chat:',chat)
            #print(nome.rjust(85))
            # print(f'idade: {idade}')
            # print(f'Tem Gmail: {gmail}')
            # print(f'Tem Outlook: {outlook}')
            # print(f'Aceita Cartão: {s_card}')
            # print(f'Não aceita Cartão: {n_card}')
            # print('=============================')
            print('\n')


tela = Tela()
tela.Iniciar()
