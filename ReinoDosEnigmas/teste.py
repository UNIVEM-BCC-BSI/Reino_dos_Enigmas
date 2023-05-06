from src.Modelo.Perguntas import *
from src.Config.funcoes import *

PerguntaRio = Questao('Com quantos Paus se faz uma canoa?\n1- um\n2- dois\n2- tres\n','tres paus','3','marcenaria','como fazer uma canoa')

PerguntaRio.exibirEnunciado()
resposta = input('Resposta: ')
PerguntaRio.verificarResposta(resposta)

print('Relatorio')

PerguntaRio.relatorio()