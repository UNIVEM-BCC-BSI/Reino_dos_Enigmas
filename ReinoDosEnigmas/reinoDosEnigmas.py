from funcoes import *
from Player import Player

def historia():
    textoAnimado('\nHavia um pirata solitário chamado', 0.02)
    textoAnimado('... ', 0.5)
    player = str(input('\nNome: '))
    player = Player(player)
    textoAnimado(f'\n{player} passou a maior parte de sua vida navegando pelos mares em busca de tesouros perdidos. Era um homem habilidoso, mas solitário, que preferia viajar sozinho em seu pequeno barco em vez de trabalhar em equipe com outros piratas. Ele acreditava que sua independência lhe dava uma vantagem sobre os outros piratas, pois não precisava dividir o tesouro com ninguém.\n\nCerto dia, {player} descobriu um mapa antigo que indicava a localização de um tesouro lendário, que se acreditava estar escondido em uma ilha remota. {player}, sendo um pirata experiente, navegou por dias sem fim pelos mares tempestuosos, enfrentando tempestades e lutando contra inimigos implacáveis, até que finalmente avistou a ilha deserta.\n\nMas infelizmente, as coisas não correram como {player} planejou. Enquanto navegava em direção à ilha, seu pequeno barco foi atingido por uma tempestade repentina e violenta, fazendo-o naufragar na costa da ilha. {player}, desesperado, conseguiu nadar até a costa, mas seu barco e todo o seu tesouro foram perdidos nas profundezas do mar.', 0.001)

    print('\n\nAo acordar na praia, jogador se vê perdido e desorientado e decide começar a andar para tentar sair da ilha o mais rápido possível. Quando ele se levanta observa que possui uma floresta densa e escura.')

    def escolhaPraia():
        print('\n\nSeguindo pela areia da praia é possível enxergar os destroços do que um dia foi o seu navio, indo mais à frente o jogador se depara com uma vegetação mais   densa e uma aparente trilha para a floresta que entes foi ignorada, ao mesmo tempo é possível ver ao horizonte altos muros de uma grande cidade.')
    
    def escolhaFloresta():
        print(f'\n\n Entrando na floresta, {player} vai andando devagar e com muito cuidado até se deparar com uma Onça, ele começa a correr com todo o seu folego e consegue encontrar uma caverna para se esconder.')
        while True:
            textoAnimado('\nQual será sua escolha?\n\n1 - Seguir correndo pela floresta \n2 - Entrar na caverna para se esconder\n\nEscolha: ', 0.02)
            escolhaParte2 = int(input())
            if escolhaParte2 == 1:
                print(f"\n\nSeguindo pela floresta {player} consegue aos poucos ir percebendo que ele estava chegando perto de uma civilização, até encontrar uma segunda trilha bem na sua frente, e para a sua surpresa ela aparentava ser bem utilizada.\nSeguindo ela o jogador em pouco tempo já se deparava com os enormes muros de uma grande cidade. Entrando nela, ele logo encontrou diversos tipos de comerciantes, guardas da cidade e grande parte da população reunida em um grande centro com uma enorme praça. \nDesesperado e com medo {player} vai atrás de ajuda conversando com um vendedor o jogador acaba descobrindo que ele é um fazendeiro que morava perto da cidade onde ele se encontrava.")
                break
            elif escolhaParte2 == 2:
                print("\n\nEntrando na caverna ele percebe que do lado contrário da caverna existe uma trilha abandonada.")
                break

    while True:
        textoAnimado('\nQual será sua escolha?\n\n1 - Seguir pela praia\n2 - Entrar na floresta\n\nEscolha: ', 0.02)
        escolhaParte1 = int(input())
        if escolhaParte1 == 1:
            escolhaPraia()
            break
        elif escolhaParte1 == 2:
            escolhaFloresta()
            break