from src.Modelo.Perguntas import *
from src.Modelo.Player import *
from src.Config.funcoes import *

nome = input('nome: ')
jogador = Player(nome,'moedas',5)

PerguntaRio = Questao('Com quantos Paus se faz uma canoa?\n1- um\n2- dois\n3- tres\n','tres paus','3','marcenaria','como fazer uma canoa')

PerguntaRio.exibirEnunciado()
resposta = input('Resposta: ')
PerguntaRio.verificarResposta(resposta)

print('Relatorio')

PerguntaRio.relatorio()






if PerguntaRio.status == True:
    print(f'\notimo {jogador.name}, a resposta esta correta, aqui está o seu premio\n')
    jogador.adicionaItem('moedas',50)
    print('moedas de ouro adicionadas na mochila')
    jogador.exibeInventario()
else:
    print(f'puxa {jogador.name}, a resposta esta errada!\n')


