import wikipedia

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

pchave = ['quem foi', 'quem é', 'quando ocorreu', 'quando aconteceu']


bot = ChatBot('Chat')
conv = ['oi',
         'ola',
         'ola, tudo bem?',
         'sim e você',
         'qual o seu nome?',
         'meu nome é Chat, e o seu?']

bot.set_trainer(ListTrainer)
bot.train(conv)


def retorno_chat(query):
    resposta = consulta(query)

    if resposta == 'Desculpe, não entendi':
        resposta = bot.get_response(query)

    return resposta

def normalizar_str(text):
    text = text.strip().lower()

    for part in pchave:
        if text.startswith(part.lower()):
            return text.replace(part, "").strip()

    return text

def consulta(query):
    query = normalizar_str(query)

    print(query)

    try:
        wikipedia.set_lang('pt')
        return wikipedia.summary(query, sentences=1)
    except:
        return 'Desculpe, não entendi'