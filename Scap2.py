# -*- coding: utf-8 -*-
from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import pprint



def pagina(url):
        pagina = get(url)
        return pagina.text

def pega_html(pagina):
    soup = bs(pagina, 'html.parser')
    boxes = soup.find_all('table', {'class': 'table table-striped table-bordered table-responsive-lg'})
    return boxes

# def pega_html(pagina):
#     soup = bs(pagina, 'html.parser')
#     boxes = soup.find_all('div', {'class': 'accordion3'})
#     return boxes


def convert_Data(boxes, lista):
    df_full = pd.read_html(str(boxes))[0].head()
    df = df_full[lista]
    df.columns = lista
    return df

def convert_json(data):
    Acao = {}
    Acao['Acoes'] = data.to_dict('records')
    js = json.dumps(Acao, ensure_ascii=False)
    return js


def cria_arquivo(nome_arq, c_json):
    arq = open(nome_arq, 'w', encoding='utf-8')
    arq.write(c_json)
    arq.close()

#url = 'https://www.arxinvestimentos.com.br/InvestmentFunds/Fund/9#tab-2'
url = 'https://www.camara.leg.br/deputados/92346/pessoal-gabinete?ano=2020'
lista = ['Nome',	'Grupo Funcional',	'Cargo/Função',	'Período de exercício',	'Remuneração mensal']
#lista = ['Dia',	'Mar-20',	'Ano',	'12 Meses',	'24 Meses',	'Desde o início']

pagina = pagina(url)
boxes = pega_html(pagina)
#print(pagina)
data = convert_Data(boxes, lista)

c_json = convert_json(data)
cria_arquivo('MaisAcao.json', c_json)


pprint.PrettyPrinter(c_json)
