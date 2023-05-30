from src.Modelo.Perguntas import *
from src.Modelo.Player import *
from src.Config.funcoes import *
from src.Modelo.questoes import *
from src.historia import *

def Barco():
    textoAnimado(f"\nA cidade pulsava com vida enquanto {jogador.name} caminhava pelas vielas estreitas, apreciando as fachadas coloridas das lojas e o som do comércio ao seu redor.\n\nAo chegar à praça central, jogador seguiu uma estrada íngreme que levava à colina da baía.\n\nAlcançando o topo, seus olhos se fixaram no estaleiro à beira-mar.\n\n\nEra um local impressionante, repleto de madeira, cordas e ferramentas.\n\nBarcos em diferentes estágios de construção espalhavam-se pelo terreno, demonstrando a dedicação e habilidade do mestre construtor.\n\n{jogador.name} foi se aproximando enquanto Lars trabalhava em um casco de madeira. O artesão estava envolto em sua tarefa, imerso em seu próprio mundo de criação.\n\nTimidamente, {jogador.name} interrompeu o artesão, que ergueu os olhos para encontrar o olhar curioso do jovem à sua frente.\n\n{GREEN+jogador.name+RESET} - Desculpe a interrupção, mestre Lars... Eu sou {jogador.name}, e ouvi falar de suas incríveis habilidades como construtor de barcos.\nVim aqui porque tenho um sonho de possuir meu próprio barco. Será que você poderia me ajudar?\n\nLars sorriu, um sorriso gentil...\n\n{BLUE+'Lars'+RESET} - Ah, meu jovem, é sempre gratificante ver alguém interessado em embarcar nessa jornada.\nTer o sonho de possuir seu próprio barco é algo especial.\nE eu ficaria feliz em ajudá-lo a transformar esse sonho em realidade.\nMas antes de começarmos, gostaria de saber mais sobre o que você está procurando.\nDiga-me, qual é o tipo de barco que você tem em mente? Quais são suas expectativas e o que pretende fazer com ele?\n\n{GREEN+jogador.name+RESET} - bem, busco um barco pequeno, minha tripulação consiste em apenas eu, e é importante também que seja rápido.\n\n{BLUE+'Lars'+RESET} - Um barco pequeno e rápido, entendo. É uma escolha excelente para aventuras individuais. Com um projeto adequado, podemos criar algo que atenda às suas necessidades.\n\n{GREEN+jogador.name+RESET} - E aproximadamente quanto custaria para o senhor construir um barco com estas esepecificações para mim?\n\n{BLUE+'Lars'+RESET} - Bem, o preço de um barco veleiro pequeno feito de madeira e adequado para os seus propositos pode variar dependendo de diversos fatores,\nmás levando em conta todos esses aspectos e considerando a viabilidade do projeto, estimo que este barco poderia custar aproximadamente 1000 moedas de ouro.\n\n{GREEN+jogador.name+RESET} - Bem... não tenho todo este dinheiro, sou novo nesta cidade...\nna verdade estou viajando a alguns dias apenas para te encontrar e poder voltar para a minha casa no outro continente...\nO senhor poderia me dar algum desconto neste valor?, quem sabe eu poderia até trabalhar aqui na oficina por alguns dias,\nou fazer qualquer coisa que o senhor me mandar!",0.01)

    textoAnimado(f"\n\n{BLUE+'Lars'+RESET} - hmmm bem, voce realmente parece interessado neste barco...\nEm minha oficina tem mutro trabalho a ser feito.\nSe voce der conta de realizar todas as terefas, conseguirei te dar um ótimo desconto.\n\n{BLUE+'Lars'+RESET} - Inclusive! a sua ajuda agora seria bem vinda.\nMais cedo eu fechei com o Rei mais uma encomenda de barcos para a frota real, e ele me passou uma série de especificações que devem ser atendidas.\nConseguiria resolver para mim estes calculos?\n\n",0.01)

    perguntaBarco.exibirEnunciado()

    while True:
        textoAnimado('\n\nResposta: ',0.01)
        escolha = (input())
        if escolha == '1':
            resposta = '1'
            break
        elif escolha == '2':
            resposta = '2'
            break
        elif escolha == '3':
            resposta = '3'
            break
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)

    perguntaBarco.verificarResposta(resposta)

    if perguntaBarco.status == True:
        textoAnimado(f"\n\n{BLUE+'Lars'+RESET} - hmm me parece promissor obrigado pela ajuda!...\n\n",0.01)
    elif perguntaBarco.status == False:
        textoAnimado(f"\n\n{BLUE+'Lars'+RESET} - hmm vou procurar mais um pouco sobre, caso precise de mais ajuda te avisarei!...\n\n",0.01)

    textoAnimado(f"\n{jogador.name} passou alguns dias dormindo na oficina e ajudando Lars enquanto admirava o trabalho do artesão com o seu barco sendo produzido.\nApós todo o tempo de seus serviços, {jogador.name} conseguiu até aprender um pouco sobre como o seu Mestre realizava seu trabalho.\n\n",0.01)

    textoAnimado(f"\n{BLUE+'Lars'+RESET} - Bem.., agora acredito que voce ja me ajudou o bastante, durante este tempo andei pensando e te observando...\nvoce realmente seria um bom navegador, e a sua ajuda foi de extrema importancia para o andamento dos meus outros projetos,\nentão indo ao que interessa, conseguirei cobrar por seu barco um valor simbolico de 500 moedas de ouro...É o minimo que conseguirei\n\n",0.01)

    

Barco()