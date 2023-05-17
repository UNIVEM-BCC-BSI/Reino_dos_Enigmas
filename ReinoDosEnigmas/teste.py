from src.Modelo.Perguntas import *
from src.Modelo.Player import *
from src.Config.funcoes import *
from src.Modelo.questoes import *

nome = input('nome: ')
jogador = Player(nome,'Moedas de ouro',5)

perguntaPraia.exibirEnunciado()
resposta = input('Resposta: ')
perguntaPraia.verificarResposta(resposta)

textoAnimado('\nRelatorio\n\n',0.01)

perguntaPraia.relatorio()


if perguntaPraia.status == True:
    print(f'\notimo {jogador.name}, a resposta esta correta, aqui está o seu premio\n')
    jogador.adicionaItem('Moedas de ouro',50)
    print('moedas de ouro adicionadas na mochila')
    jogador.exibeInventario()
    jogador.aumentaPonto('geografia')
else:
    print(f'puxa {jogador.name}, a resposta esta errada!\n')
    jogador.aumentaPonto('matematica')

print('pontos de geografia: ' ,jogador.pontosGeo)
print('pontos de matematica: ', jogador.pontosMat)

