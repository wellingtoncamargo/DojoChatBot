import wikipedia

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot



bot = ChatBot('Chat')
pchave = ['quem foi', 'quem é', 'quando ocorreu', 'quando aconteceu']
conv = ['oi',
         'ola',
         'ola, tudo bem?',
         'sim e você',
         'qual o seu nome?',
         'meu nome é Chat, e o seu?']


def aprender():
    bot.set_trainer(ListTrainer)
    bot.train(conv)


def retorno_chat(query):
    resposta = bot.get_response(query)
    if float(resposta.confidence) > 0.7:
        return resposta
    else:
        resposta = consulta(query)
        return resposta

def normalizar_str(text):
    text = text.strip().lower()

    for part in pchave:
        if text.startswith(part.lower()):
            return text.replace(part, "").strip()

    return text


def consulta(query):
    query = normalizar_str(query)

    try:
        wikipedia.set_lang('pt')
        return wikipedia.summary(query, sentences=1)
    except:
        return 'Desculpe, não entendi'