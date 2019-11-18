# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Senior')
conv2 = ['oi',
         'ola',
         'ola, tudo bem?',
         'sim e você',
         'qual o seu nome?',
         'meu nome é Chat, e o seu?']

bot.set_trainer(ListTrainer)
bot.train(conv2)

while True:
    quest = input('Voce: ')
    resp = bot.get_response(quest)

    if float(resp.confidence) > 0.5:
        print('Chat: ', resp)
    else:
        print('Chat: Desculpe, não entendi')