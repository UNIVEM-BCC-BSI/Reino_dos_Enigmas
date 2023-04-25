from funcoes import *
from reinoDosEnigmas import *
import time,sys

pontoGeografia = 0
pontoMatematica = 0

while True:
    print("""
             O Reino dos Enigmas

            1 - Iniciar jogo
            2 - Sobre
            3 - Créditos
            4 - Sair
        """)
    textoAnimado('Escolha: ',0.08)
    escolhaInicio = int(input())
    if escolhaInicio == 1:
        historia()
        break
    elif escolhaInicio == 2:
        print('\nO jogador vivencia um pirata que viaja pelas cidades do Reino dos Enigmas em busca de ao longo do caminho conseguir lucros para ao final da sua jornada conseguir comprar um novo barco e retornar para a sua casa em um outro reino cruzando o oceano.\nCaso o contrário, as autoridades conseguirão o capturar.\nAo longo do caminho podem ser encontrados eventos, como ladrões que podem roubar suas posses, mercados e quests.\nDentro de cada um dos eventos são exibidas perguntas que modificam o andamento da historia de acordo com a resposta do usuário ou modificar o seu inventario.\nAo longo da jornada todo o seu dinheiro obtido será revertido em pontos obtidos, e uma tela apresentará um relatório das suas respostas ao longo da jornada, exibindo quais foram as dificuldades do jogador.')
            
        textoAnimado('\nDigite qualquer numero para voltar: ', 0.08)
        int(input())

    elif escolhaInicio == 3:
        print("""
            Henry Lacava
            Otavio Sbms
            Juan Yang
            Guilherme Silva
            Yukio Mawatari""")

        textoAnimado('\nDigite qualquer numero para voltar: ', 0.08)
        int(input())
            
    elif escolhaInicio == 4:
        print("Obrigado por jogar!")
        quit()
