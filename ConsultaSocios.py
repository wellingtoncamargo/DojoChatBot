# -*- coding: utf-8 -*-
from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
from pprint import pprint

_url = 'https://www.consultasocio.com/q/sa/neide-aparecida-dos-santos'

cont = get(_url).content
soap = bs(cont, 'html.parser')
obj = dict()
for texto in soap.find_all('div',{'class': 'info'}):
    obj.setdefault('Empresa',texto.h3.text)
    obj.setdefault('Nome',texto.p.text)
    for p in texto.find_all('p'):
        keys = p.text.split(':')
        # print(keys[0])
        if 'Neide' in keys[0] or 'Não há' in keys[0]:
            pass
        else:
            # print(keys[0],keys[1])
            obj.setdefault(keys[0], keys[1])
pprint(obj, sort_dicts=False)
# info = texto.find_all()/