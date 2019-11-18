# -*- coding: utf-8 -*-

import speech_recognition as sr
import wikipedia
import pyttsx3
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot2 = ChatBot('Senior')
conv2 = ['oi',
         'ola',
         'ola, tudo bem?',
         'sim e você',
         'qual o seu nome?',
         'meu nome é Chat, e o seu?']

    bot2.set_trainer(ListTrainer)
    bot2.train(conv2)
    print('Chat: Olá o que quer saber?')
    while True:

        audio = r.listen(s)

        speech = r.recognize_google(audio, language='pt-BR')
        print('Eu:',speech)
        res = evaluate(speech)

        if res is not None:
            ans = answer(speech)
            print('Chat:',ans)
            speak(ans)
            print()

        elif True:
            resp = bot2.get_response(speech)
            print('Chat:', resp)
            speak(resp)
        else:
            print('Chat: Desculpe, não entendi!')
            speak('Desculpe, não entendi!')