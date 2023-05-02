from funcoes import *
from Player import *

RED   = "\033[1;31m"
RESET = "\033[0;0m"
BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"

player = str(input('\nNome: '))
playerClass = Player(player)

def intro():
    textoAnimado(f'\n{playerClass.name} passou a maior parte de sua vida navegando pelos mares em busca de tesouros perdidos. Era um homem habilidoso, mas solitário, que preferia viajar sozinho em seu pequeno barco em vez de trabalhar em equipe com outros piratas. Ele acreditava que sua independência lhe dava uma vantagem sobre os outros piratas, pois não precisava dividir o tesouro com ninguém.\n\nCerto dia, {playerClass.name} descobriu um mapa antigo que indicava a localização de um tesouro lendário, que se acreditava estar escondido em uma ilha remota. {playerClass.name}, sendo um pirata experiente, navegou por dias sem fim pelos mares tempestuosos, enfrentando tempestades e lutando contra inimigos implacáveis, até que finalmente avistou a ilha deserta.\n\nMas infelizmente, as coisas não correram como {playerClass.name} planejou. Enquanto navegava em direção à ilha, seu pequeno barco foi atingido por uma tempestade repentina e violenta, fazendo-o naufragar na costa da ilha. {playerClass.name}, desesperado, conseguiu nadar até a costa, mas seu barco e todo o seu tesouro foram perdidos nas profundezas do mar.', 0.001)

    print(f'\n\nAo acordar na praia, {playerClass.name} se vê perdido e desorientado, e decide começar a andar para tentar sair da ilha o mais rápido possível. Quando ele se levanta observa que existe uma floresta densa e escura.')

def caverna():
    textoAnimado(f"\n\nEntrando na caverna ele percebe que do lado contrário da caverna existe uma trilha abandonada.\nDentro da caverna {playerClass.name} se depara com um mineiro...",0.08)
    textoAnimado(f"\n- Mineiro: O que você está fazendo aqui?\n- {playerClass.name}: Me deparei com uma cobra muito grande e comecei a correr\n- Mineiro: Grande?!!, láá ele\n- Mineiro: Aqui na região possui muitas cavernas, e ja ganhei muito dinheiro minerando por elas. Você sabe como surgem as cavernas?")

def cidade():
    print(f"\n\nSeguindo pela floresta {playerClass.name} consegue aos poucos ir percebendo que a vegetação ao seu redor estava mudando, até encontrar uma segunda trilha bem a sua frente, e para a sua surpresa ela aparentava ser bem utilizada.\n Seguindo ela, {playerClass.name} em pouco tempo já se deparava com os enormes muros de uma grande cidade. Adentrando-a, a primeira coisa que chamou a atenção foram os diversos tipos de comerciantes, guardas da cidade e a população reunida em um grande centro com uma praça.\n Desesperado e com medo {playerClass.name} vai atrás de uma ajuda o mais rápido possivel, onde acaba abordando um vendedor em sua barraca de legumes.\n\n {BLUE+'vendedor'+RESET} - Saldações viajante!, o que deseja comprar?\n\n {GREEN+playerClass.name+RESET} - Olá, acabo de chegar nesta cidade e gostaria de saber onde poderia me hospedar.\n\n {BLUE+'vendedor'+RESET} - Ora, a cidade está muito movimentada devido a grandiosa chegada do principe, o filho do rei finalmente retornou depois de uma de suas grandes cavalgadas. Sinto em lhe dizer viajante, más todas as hospedarias da cidade estão ocupadas, a festa será grandiosa!\n\n {GREEN+playerClass.name+RESET} - Não estava sabendo deste evento, estava passando apenas de viagem e iria embora logo ao amanhecer, o senhor conheceria alguem que pudesse me ceder um local para dormir?\n\n o vendedor encara {playerClass.name} da cabeça aos pés...\n\n {BLUE+'vendedor'+RESET} - Bem jovem... estou aqui apenas a trabalho, moro em uma pequena fazenda seguindo ao Norte.\n Entendo a sua situação, um dia eu já fui como voçe, apenas um viajante entre as cidades.\n caso o interesse, o Celeiro de minha fazenda talvez possa te abrigar por hoje.\n\n {GREEN+playerClass.name+RESET} - Claro Senhor! seria um favor enorme...\n")

def Praia():
    print(f'\n\nSeguindo pela areia da praia é possível enxergar os destroços do que um dia foi o seu navio, indo mais à frente {playerClass.name} se depara com uma vegetação mais densa e uma aparente trilha para a floresta que entes foi ignorada, ao mesmo tempo é possível ver ao horizonte altos muros de uma grande cidade.')

def Floresta():
    print(f'\n\n Entrando na floresta, {playerClass.name} vai andando devagar e com muito cuidado até se deparar com um enorme Javali selvagem em meio a vegetação. No intuito de tentar escapar sem quel o animal o perceba, {playerClass.name} tenta sair dali o mais rápido possivel, porem já era tarde demais e o Javali começa o perseguir. {playerClass.name} corre com todo o seu folego até encontrar em meio a densa floresta uma caverna.')
    while True:
        textoAnimado('\nQual será sua escolha?\n\n1 - Seguir correndo pela floresta \n2 - Entrar na caverna\n\nEscolha: ', 0.02)
        escolhaParte2 = (input())
        if escolhaParte2 == '1':
            cidade()
            break
        elif escolhaParte2 == '2':
            caverna()
            break
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)

def historia():

    intro()

    while True:
        textoAnimado('\nQual será sua escolha?\n\n1 - Seguir pela praia\n2 - Entrar na floresta\n\nEscolha: ', 0.02)
        escolhaParte1 = (input())
        if escolhaParte1 == '1':
            Praia()
            break
        elif escolhaParte1 == '2':
            Floresta()
            break
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)
