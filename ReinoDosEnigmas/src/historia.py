from src.Config.funcoes import *
from src.Modelo.Player import *

player = str(input('\nNome: '))
jogador = Player(player,'Moedas de ouro',5)

from src.Modelo.questoes import *

def intro():
    textoAnimado(f'\n{jogador.name} passou a maior parte de sua vida navegando pelos mares em busca de tesouros perdidos. Era um homem habilidoso, mas solitário, que preferia viajar sozinho em seu pequeno barco em vez de trabalhar em equipe com outros piratas. Ele acreditava que sua independência lhe dava uma vantagem sobre os outros piratas, pois não precisava dividir o tesouro com ninguém.\n\nCerto dia, {jogador.name} descobriu um mapa antigo que indicava a localização de um tesouro lendário, que se acreditava estar escondido em uma ilha remota. {jogador.name}, sendo um pirata experiente, navegou por dias sem fim pelos mares tempestuosos, enfrentando tempestades e lutando contra inimigos implacáveis, até que finalmente avistou a ilha deserta.\n\nMas infelizmente, as coisas não correram como {jogador.name} planejou. Enquanto navegava em direção à ilha, seu pequeno barco foi atingido por uma tempestade repentina e violenta, fazendo-o ter que mudar completamente o seu caminho, nalfraando na costa do continente. {jogador.name}, desesperado, conseguiu nadar até a praia, mas seu barco e todo o seu tesouro foram perdidos nas profundezas do mar, restando apenas consigo uma mochila com alguns itens que sobraram.',0.01)

    textoAnimado(f'\n\nAo acordar na praia, {jogador.name} se vê perdido e desorientado, e decide começar a andar para tentar sair daquele lugar o mais rápido possível. Quando ele se levanta observa que a praia se extendia por quilómetros a sua frente, e uma floresta densa e escura acompanhava ela por toda a sua extenção.',0.01)

def caverna():

    textoAnimado(f"\n{jogador.name} decide ignorar a trilha e se esconder no lugar mais próximo possivel.\nDentro da caverna {jogador.name} percebe que o ambiente um dia já havia sido uma grande mineração, porém hoje ela estava abandonada e com várias ferramentas antigas e carrinhos cheios de pedra por toda parte.\nExplorando mais o local em busca de uma saida, ao fundo de uma fenda, {jogador.name} consegue vizualizar uma luz fraca de um lampião.\nChegando mais perto ainda, ele se depara com um Anão com uma enorme barba branca vestindo um macacão sujo e com uma picareta, inpecionando um pequeno cristal transparente. {jogador.name} fica com medo mas percebe que o velho Anão minerador não poderia ser um problema maior do que o Javali do lado de fora da caverna, e resolve ir falar com ele...",0.01)
    textoAnimado(f"\n\n{GREEN+jogador.name+RESET} - O..Olá?...\n\n O Anão minerador olha para {jogador.name} e da um pulo de susto...\n\n{BLUE+'Minerador'+RESET} - MEU DEUS!, quem lhe contou que eu estava aqui?? Por acaso te falaram alguma coisa sobre mim???\n\n{GREEN+jogador.name+RESET} - Não não senhor..., eu só entrei aqui procurando um lugar para me esconder, lá fora tem um Javali que está me perseguindo\n\n{BLUE+'Minerador'+RESET} - Um Javali?, voce entrou nesta antiga mina abandonada só por causa de um Javali?\n\n{GREEN+jogador.name+RESET} - Sim...\n\n{BLUE+'Minerador'+RESET} - hmm, bem, já que voce está por aqui, finja que nunca me viu, tenho muito trabalho por aqui.\n\n{GREEN+jogador.name+RESET} - Más o que o senhor está fazendo? preciso de ajuda urgente!, meu tempo é curto e preciso encontrar um local para dormir.\n\n{BLUE+'Minerador'+RESET} - Voce fala demais para o meu gosto eim 'viajante'...\nAposto que foi mandado pelos meus irmãos para me vijiar, más como esta caverna não é para amadores como voce, resolva o meu enigma e eu penso se te mostro a saida.\n\n{jogador.name} fica confuso más aceita o pedido, afinal, não teria como a situação ficar pior.\n\n{GREEN+jogador.name+RESET} - Ok, eu ajudo.\n",0.01)

    perguntaCaverna.exibirEnunciado()
    resposta = input('Resposta: ')
    perguntaCaverna.verificarResposta(resposta)
    
    if perguntaCaverna.status == True:
        textoAnimado(f"\n{BLUE+'Minerador'+RESET} - Hmm, me parece que voce não é tão tolo quanto eu imaginava, a resposta está correta, pegue tambem este premio:\n",0.01)
        jogador.adicionaItem('Moeda de ouro',50)
        textoAnimado('\nmoedas de ouro adicionadas na mochila',0.01)
        jogador.exibeInventario()
        textoAnimado(f"\n\n{BLUE+'Minerador'+RESET} - Me siga por este caminho.\n\n{jogador.name} segue o Velho em meio a escuridão, tendo o caminho iluminado apenas por um lampião velho.\n\n{BLUE+'Minerador'+RESET} - A saida não está muito longe.\n\nApós alguns minutos de caminhada ao fundo era possivel ver uma luz, chegando mais perto {jogador.name} já estava na saida.\n\n{BLUE+'Minerador'+RESET} - Vá e não volte, mais a frente existe uma trilha, siga ela.\n\nAntes mesmo que {jogador.name} pudesse se agradecer, o Minerador já havia voltado para o seu trabalho...\n\n{GREEN+jogador.name+RESET} - Muito obrigado senhor.. Senhor?\n\n",0.01)
        input('Digite para continuar: ')
        cidade()
    else:
        textoAnimado(f"\n{BLUE+'Minerador'+RESET} - Eu já esperava... a resposta está errada!\n{BLUE+'Minerador'+RESET} - hmm, pensando bem voce não parece ter sido enviado...\n{BLUE+'Minerador'+RESET} - De qualquer forma vou te mostrar o caminho, logo ficará de noite e tambem tenho que ir.\n",0.01)
        textoAnimado(f"\n\n{BLUE+'Minerador'+RESET} - Me siga por este caminho.\n\n{jogador.name} segue o Velho em meio a escuridão, tendo o caminho iluminado apenas por um lampião velho.\n\n{BLUE+'Minerador'+RESET} - A saida não está muito longe.\n\nApós alguns minutos de caminhada ao fundo era possivel ver uma luz, chegando mais perto {jogador.name} já estava na saida.\n\n{BLUE+'Minerador'+RESET} - Vá e não volte, mais a frente existe uma trilha, siga ela.\n\nAntes mesmo que {jogador.name} pudesse se agradecer, o Minerador já havia voltado para o seu trabalho...\n\n{GREEN+jogador.name+RESET} - Muito obrigado senhor.. Senhor?\n\n",0.01)
        input('Digite para continuar: ')
        cidade()

def cidade():
    textoAnimado(f"\n\nSeguindo pela floresta {jogador.name} consegue aos poucos ir percebendo que a vegetação ao seu redor estava mudando, até encontrar uma segunda trilha bem a sua frente, e para a sua surpresa ela aparentava ser bem utilizada.\n Seguindo ela, {jogador.name} em pouco tempo já se deparava com os enormes muros de uma grande cidade. Adentrando-a, a primeira coisa que chamou a atenção foram os diversos tipos de comerciantes, guardas da cidade e a população reunida em um grande centro com uma praça.\n\nDesesperado e com medo {jogador.name} vai atrás de uma ajuda o mais rápido possivel, onde acaba abordando um vendedor em sua barraca de legumes.\n\n {BLUE+'Vendedor'+RESET} - Saudações viajante!, o que deseja comprar?\n\n {GREEN+jogador.name+RESET} - Olá, acabo de chegar nesta cidade e gostaria de saber onde poderia me hospedar.\n\n {BLUE+'Vendedor'+RESET} - Ora, a cidade está muito movimentada devido a grandiosa chegada do principe, o filho do rei finalmente retornou depois de uma de suas grandes cavalgadas. Sinto em lhe dizer viajante, más todas as hospedarias da cidade estão ocupadas, a festa será grandiosa!\n\n {GREEN+jogador.name+RESET} - Não estava sabendo deste evento, estava passando apenas de viagem e iria embora logo ao amanhecer, o senhor conheceria alguem que pudesse me ceder um local para dormir?\n\n o vendedor encara {jogador.name} da cabeça aos pés...\n\n {BLUE+'Vendedor'+RESET} - Bem jovem... estou aqui apenas a trabalho, moro em uma pequena fazenda seguindo ao Norte.\n Entendo a sua situação, um dia eu já fui como voçe, apenas um viajante entre as cidades.\n caso o interesse, o Celeiro de minha fazenda talvez possa te abrigar por hoje.\n\n {GREEN+jogador.name+RESET} - Claro Senhor! seria um favor enorme...\n\n",0.01)
    input('Digite para continuar: ')
    fazenda()

def fazenda():
    textoAnimado("\naalhsdilashdashldhliasdyhilsadliash",0.01)

def Praia():
    textoAnimado(f'\n\nSeguindo pela areia da praia é possível enxergar os destroços do que um dia foi o seu barco, indo mais à frente {jogador.name} se depara com uma vegetação mais densa e uma aparente trilha para a floresta que entes foi ignorada, ao mesmo tempo é possível ver ao horizonte altos muros de uma grande cidade.',0.01)

def Floresta():
    textoAnimado(f'\nEntrando na floresta, {jogador.name} vai andando devagar e com muito cuidado até se deparar com um enorme Javali selvagem em meio a vegetação. No intuito de tentar escapar sem quel o animal o perceba, {jogador.name} tenta sair dali o mais rápido possivel, porem já era tarde demais e o Javali começa o perseguir. {jogador.name} corre com todo o seu folego até encontrar uma encrisilhada em meio a densa floresta, onde havia uma caverna e lado contrário uma trilha abandonada.',0.01)
    while True:
        textoAnimado('\nQual será sua escolha?\n\n1 - Seguir correndo pela floresta \n2 - Entrar na caverna\n\nEscolha: ',0.01)
        escolhaParte2 = (input())
        if escolhaParte2 == '1':
            cidade()
            break
        elif escolhaParte2 == '2':
            caverna()
            print('\nPERGUNTA SOBRE A GEOGRAFIA DA CAVERNA.\n')
            break
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)

def historia():

    intro()

    while True:
        textoAnimado('\nQual será sua escolha?\n\n1 - Seguir pela praia\n2 - Entrar na floresta\n\nEscolha: ',0.01)
        escolhaParte1 = (input())
        if escolhaParte1 == '1':
            Praia()
            break
        elif escolhaParte1 == '2':
            Floresta()
            break
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)
