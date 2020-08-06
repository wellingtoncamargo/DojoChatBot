# -*- coding: utf-8 -*-
from Consulta import retorno_chat, consulta

while True:
    quest = input('Voce: ')
    resp = retorno_chat(quest)
    print('Chat: ', resp)
