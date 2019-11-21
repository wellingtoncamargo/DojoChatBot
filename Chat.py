# -*- coding: utf-8 -*-
from Consulta import retorno_chat

while True:
    quest = input('Voce: ')
    resp = retorno_chat(quest)

    if float(resp.confidence) > 0.5:
        print('Chat: ', resp)
    else:
        print('Chat: Desculpe, não entendi')