# -*- coding: utf-8 -*-
from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
from pprint import pprint



Acao = {
        'tabela_1': {'Nome da Ação':'Nome da Ação', 'Código da Ação':'Código da Ação', 'Bolsa de Valores':'Bolsa de Valores', 'Tipo de Ativo':'Tipo de Ativo', 'Código ISIN do Ativo':'Código ISIN do Ativo', 'Descrição da Ação':'Descrição da Ação'},
        'tabela_2': {'Variação do Dia (p)':'Variação do Dia (p)', 'Variação do Dia %':'Variação do Dia %','Último Preço':'Último Preço', 'Preço de Fechamento':'Preço de Fechamento','Hora':'Hora'},
        'tabela_3': {'Melhor Preço de Compra':'Melhor Preço de Compra', 'Melhor Preço de Venda':'Melhor Preço de Venda','Spread de Preço':'Spread de Preço', 'Spread de Preço %':'Spread de Preço %'},
}

def buildAcoes(type, i):
        pagina = get('https://www.camara.leg.br/deputados/92346/pessoal-gabinete?ano=2020').content
        soup = bs(pagina, 'html.parser')
        boxes = soup.find_all('div', {'class':"table table-striped table-bordered table-responsive-lg"})


        df_full = pd.read_html(str(boxes))[i]
        df = df_full[[type]]
        df.columns = [type]

        return df.to_dict('records')
#
# i = 0
l  = 'Nome', 'Grupo Funcional', 'Cargo/Função', 'Período de exercício', 'Remuneração mensal'
# for a in l:
#         if i != 3:
#             Acao[a] = buildAcoes(a, i)
#             i+=1
#for i in l:
#print(i)
js = json.dumps(l, ensure_ascii=False)
arq = open('MaisAcao.json', 'w', encoding='utf-8')
#arq.write(js.replace('}, {',','))
arq.write(js)
#arq.write(js)
arq.close()

print(js)


