from src.Config.funcoes import *
from src.Modelo.Player import *

player = str(input('\nNome: '))
jogador = Player(player,'Moedas de ouro',50)

from src.Modelo.questoes import *

def intro():
    textoAnimado(f'\n{jogador.name} passou a maior parte de sua vida navegando pelos mares em busca de tesouros perdidos. Era um homem habilidoso, mas solitário, que preferia viajar sozinho em seu pequeno barco em vez de trabalhar em equipe com outros piratas. Ele acreditava que sua independência lhe dava uma vantagem sobre os outros piratas, pois não precisava dividir o tesouro com ninguém.\n\nCerto dia, {jogador.name} descobriu um mapa antigo que indicava a localização de um tesouro lendário, que se acreditava estar escondido em uma ilha remota. {jogador.name}, sendo um pirata experiente, navegou por dias sem fim pelos mares tempestuosos, enfrentando tempestades e lutando contra inimigos implacáveis, até que finalmente avistou a ilha deserta.\n\nMas infelizmente, as coisas não correram como {jogador.name} planejou. Enquanto navegava em direção à ilha, seu pequeno barco foi atingido por uma tempestade repentina e violenta, fazendo-o ter que mudar completamente o seu caminho, nalfraando na costa do continente. {jogador.name}, desesperado, conseguiu nadar até a praia, mas seu barco e todo o seu tesouro foram perdidos nas profundezas do mar, restando apenas consigo uma mochila com alguns itens que sobraram.',0.01)

    textoAnimado(f'\n\nAo acordar na praia, {jogador.name} se vê perdido e desorientado, e decide começar a andar para tentar sair daquele lugar o mais rápido possível. Quando ele se levanta observa que a praia se extendia por quilómetros a sua frente, e uma floresta densa e escura acompanhava ela por toda a sua extenção.',0.01)

    while True:
        textoAnimado('\nQual será sua escolha?\n\n1 - Seguir correndo pela Praia \n2 - Entrar na floresta\n\nEscolha: ',0.01)
        escolha = (input())
        if escolha == '1':
            Praia()
            break
        elif escolha == '2':
            Floresta()
            break
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)

def Praia():
    textoAnimado(f'\n\nSeguindo pela areia da praia é possível enxergar os destroços do que um dia foi o seu barco, indo mais à frente {jogador.name} se depara com uma vegetação mais densa e uma aparente trilha para a floresta que entes foi ignorada, ao mesmo tempo é possível ver ao horizonte altos muros de uma grande cidade.\n\nAo observar por mais algum tempo o oceno, {jogador.name} observa que a água parecia estar um pouco mais rasa do que ela se encontrava agora, más ignora o acontecimento.\n',0.01)
    perguntaPraia.exibirEnunciado()

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

    perguntaPraia.verificarResposta(resposta)
    if perguntaPraia.status == True:
        jogador.darPontos("Geografia")

    input('\nDigite para continuar: ')
    Floresta()

def Floresta():
    textoAnimado(f"\nEntrando na floresta, {jogador.name} vai andando devagar e com muito cuidado, olhando todas aquelas arvores e vegetação, {jogador.name} fica impressioonado com o tamanho da floresta",0.01)

    perguntaFloresta.exibirEnunciado()

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

    perguntaFloresta.verificarResposta(resposta)
    if perguntaFloresta.status == True:
        jogador.darPontos("Geografia")


    textoAnimado(f"{jogador.name} Continua andando até se deparar com um enorme Javali selvagem em meio a vegetação. No intuito de tentar escapar sem quel o animal o perceba, {jogador.name} tenta sair dali o mais rápido possivel, porem já era tarde demais e o Javali começa o perseguir. {jogador.name} corre com todo o seu folego até encontrar uma encrusilhada em meio a densa floresta, onde havia uma caverna e lado contrário uma trilha abandonada.",0.01)
    while True:
        textoAnimado('\nQual será sua escolha?\n\n1 - Seguir correndo pela floresta \n2 - Entrar na caverna\n\nEscolha: ',0.01)
        escolhaParte2 = (input())
        if escolhaParte2 == '1':
            cidade()
            break
        elif escolhaParte2 == '2':
            caverna()
            break
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)

def caverna():
    textoAnimado(f"\n{jogador.name} decide ignorar a trilha e se esconder no lugar mais próximo possivel.\nDentro da caverna {jogador.name} percebe que o ambiente um dia já havia sido uma grande mineração, porém hoje ela estava abandonada e com várias ferramentas antigas e carrinhos cheios de pedra por toda parte.\nExplorando mais o local em busca de uma saida, ao fundo de uma fenda, {jogador.name} consegue vizualizar uma luz fraca de um lampião.\nChegando mais perto ainda, ele se depara com um Anão com uma enorme barba branca vestindo um macacão sujo e com uma picareta, inpecionando um pequeno cristal transparente. {jogador.name} fica com medo mas percebe que o velho Anão minerador não poderia ser um problema maior do que o Javali do lado de fora da caverna, e resolve ir falar com ele...",0.01)
    textoAnimado(f"\n\n{GREEN+jogador.name+RESET} - O..Olá?...\n\n O Anão minerador olha para {jogador.name} e da um pulo de susto...\n\n{BLUE+'Minerador'+RESET} - MEU DEUS!, quem lhe contou que eu estava aqui?? Por acaso te falaram alguma coisa sobre mim???\n\n{GREEN+jogador.name+RESET} - Não não senhor..., eu só entrei aqui procurando um lugar para me esconder, lá fora tem um Javali que está me perseguindo\n\n{BLUE+'Minerador'+RESET} - Um Javali?, voce entrou nesta antiga mina abandonada só por causa de um Javali?\n\n{GREEN+jogador.name+RESET} - Sim...\n\n{BLUE+'Minerador'+RESET} - hmm, bem, já que voce está por aqui, finja que nunca me viu, tenho muito trabalho por aqui.\n\n{GREEN+jogador.name+RESET} - Más o que o senhor está fazendo? preciso de ajuda urgente!, meu tempo é curto e preciso encontrar um local para dormir.\n\n{BLUE+'Minerador'+RESET} - Voce fala demais para o meu gosto eim 'viajante'...\nAposto que foi mandado pelos meus irmãos para me vijiar, más como esta caverna não é para amadores como voce, resolva o meu enigma e eu penso se te mostro a saida.\n\n{jogador.name} fica confuso más aceita o pedido, afinal, não teria como a situação ficar pior.\n\n{GREEN+jogador.name+RESET} - Ok, eu ajudo.\n",0.01)

    perguntaCaverna.exibirEnunciado()

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

    perguntaCaverna.verificarResposta(resposta)
    
    if perguntaCaverna.status == True:
        jogador.darPontos("Geografia")
        textoAnimado(f"\n{BLUE+'Minerador'+RESET} - Hmm, me parece que voce não é tão tolo quanto eu imaginava, a resposta está correta, pegue tambem este premio:\n",0.01)
        jogador.adicionaItem('Moedas de ouro',50)
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
    Fazenda()

def Fazenda():

    textoAnimado(f"\nAo chegar na fazenda durante o anoitecer, o fazendeiro apresenta a {jogador.name} onde será a sua estadia, e o dia se encerra com o mesmo dormindo cansado ao lado dos animais do celeiro.",0.01)
    textoAnimado('\n\n......', 0.5)
    textoAnimado(f"\n\nNo outro dia, {jogador.name} é acordado cedo pelos galos e ao sair do celeiro já encontra o fazendeiro trabalhando em sua fazenda.\n\nAo agradecer pela estadia, no intuito de continuar a sua jornada, {jogador.name} é surpreendido pelo fazendeiro dizendo que o preço por sua hospedagem seria pago por auxílios e trabalhos na fazenda.\n\nDurante algumas horas, {jogador.name} limpou todo o celeiro e alimentou os animais do fazendeiro.\n\nEnquanto {jogador.name} trabalhava, foi possivel escutar o Fazendeiro resmungando sobre como ele faria a nova cerca da sua propriedade.\n\n\n{GREEN+jogador.name+RESET} - Com licensa senhor, o que voce esta tentando calcular?\n\n{BLUE+'Fazendeiro'+RESET} - Estou planejando quanto arame terei que comprar, odeio gastar mais dinheiro do que deveria, e ele não pode faltar.\n\n{GREEN+jogador.name+RESET} - hmmm eu acho q consigo te ajudar.\n\n",0.01)

    perguntaFazenda.exibirEnunciado()

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

    perguntaFazenda.verificarResposta(resposta)


    if perguntaFazenda.status == True:
        jogador.darPontos("Matematica")
        textoAnimado(f"\n{BLUE+'Fazendeiro'+RESET} - Nossa!, nunca tinha parado para pensar assim.\npegue estas moedas como forma de pagamento. A sua ajuda foi maior do que eu imaginava.",0.01)
        jogador.adicionaItem('Moedas de ouro',80)
        textoAnimado('\n\nmoedas de ouro adicionadas na mochila',0.01)
        jogador.exibeInventario()
        textoAnimado(f'\n{GREEN+jogador.name+RESET} - Muito obrigado senhor!',0.01)
    else:
        textoAnimado(f"\n{BLUE+'Fazendeiro'+RESET} - hmm não sei.. senho minhas duvidas, mas de quelquer forma, obrigado pela ajuda.\npode seguir em frente a sua viajem.",0.01)
        textoAnimado(f'\n\n{GREEN+jogador.name+RESET} - Muito obrigado senhor!',0.01)

    textoAnimado(f"\n\nApós aquela exaustiva manhã de trabalho duro, o {jogador.name} finalmente é liberado da fazenda e conseguiu continuar o seu caminho.\n",0.01)
    input('\nDigite para continuar: ')
    Rio()

def Rio():
    textoAnimado(f"\n\nSaindo da fazenda e seguindo uma estrada por algumas horas, {jogador.name} encontra um rio.\n\n{jogador.name} também notou que o rio contornava os locais por onde já havia passado e agora ele estava chegando em seu fim, indo em direção ao oceano.\n",0.01)
    
    perguntaRio.exibirEnunciado()

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

    perguntaRio.verificarResposta(resposta)

    if perguntaRio.status == True:
        jogador.darPontos("Geografia")

    textoAnimado(f"\nContinuando com cuidado pela margem, em pouco tempo {jogador.name} conseguiu encontrar canais de irrigação que saíam do rio, logo poderia existir uma civilização pelas redondezas.\n\nSeguindo mais a fundo, ao longo do canal, um padrão improvável acaba também chamando a atenção de {jogador.name}.\n\nUm desvio nos canais feitos de pedra levava a uma tubulação improvisada feita de bambu em direção ao campo.\n",0.01)


    while True:
        textoAnimado('\nQual será sua escolha?\n\n1 - Seguir os canais de pedra\n2 - Seguir a tubulação de Bamboo\n\nEscolha: ',0.01)
        escolhaParte2 = (input())
        if escolhaParte2 == '1':
            CidadePequena()
            break
        elif escolhaParte2 == '2':
            CasaIsolada()
            break
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)

def CidadePequena():
    textoAnimado(f"\n\nSeguindo os canais de irrigação, no horizonte {jogador.name} já consegue enxergar uma nova cidade em seu caminho.\nEsta nova cidade ao contrário da primeira cidade visitada pelo {jogador.name}. era pequena e com poucos habitantes.\nNo centro dela também havia uma Feira, onde chamou a atenção de {jogador.name} a grande quantidade de frutos do mar e peixes que eram vendidos.\nPensando nisso, {jogador.name} pergunta a um habitante local o quão perto ele já se sencontrava do Oceano. e acaba descobrindo que ele estaria a poucas horas do litoral e de uma das maiores cidades do reino.\n\n Com isso, {jogador.name} continua a sua jornada agora mais confiante de ter o seu objetivo concluído.", 0.01)
    input('\nDigite para continuar: ')
    CidadeDoMar()

def CasaIsolada():
    textoAnimado(f"\nSeguindo a tubulação improvisada, {jogador.name} anda por alguns minutos até encontrar uma pequena cabana feita de madeira isolada em meio a um campo.\nCurioso, {jogador.name} decide se aproximar e bater na porta. Para sua surpresa, um velho vestindo trapos e com uma barba longa abriu a porta.\n\n{BLUE+'Velho'+RESET}- Quem é?\n\n{GREEN+jogador.name+RESET}- Oi.. achei que a casa estava vazia..\n\n{BLUE+'Velho'+RESET}- Sim, mas não está, tenha um bom dia.\n\n{GREEN+jogador.name+RESET}- Espere, preciso de ajuda.\n\n{BLUE+'Velho'+RESET}- hmm que tipo de ajuda?\n\n{GREEN+jogador.name+RESET}- sou um viajante e preciso de um lugar para dormir, o senhor sabe onde posso arrumar um abrigo?\n\n{BLUE+'Velho'+RESET}- hmm por aqui não tem nada além de um pequeno povoado mais ao norte, mas a estrada estas horas costuma ser bem perigosa.\n\n{GREEN+jogador.name+RESET}- Então eu poderia passar só esta noite aqui?\n\nO velho analisa {jogador.name} dos pés a cabeça. Algo entre os dois parecia familiar, então pela surpresa dele mesmo, o pedido de {jogador.name} foi aceito.\n\n{BLUE+'Velho'+RESET}- aahh tabom, mas só por hoje...\n\n{jogador.name} ao entrar consegue ver uma cabana muito humilde, com utencilios de navegação, um chapéu e um papagaio em uma gaiola com apenas um olho aberto.\n\n{jogador.name} também nota que o estranho velho andava mancando pois possuia uma perna de pau.\nDepois destas descobertas {jogador.name} disse:\n\n{GREEN+jogador.name+RESET}- Ei, o senhor navegava?\n\n{BLUE+'Velho'+RESET}- Eu ja fui um aventureiro, acho q pode-se dizer assim...\n\n{GREEN+jogador.name+RESET}- hmm que tipo de aventureiro marujo?\n\n{BLUE+'Velho'+RESET}- Marujo?? como ousa me chamar assim, eu mandava neste mar!\n\n{GREEN+jogador.name+RESET}- Eu sabia que algo estav diferente, desculpe senhor mas qual é o seu nome?\n\n{BLUE+'Velho'+RESET}- Eu já tive varios nomes, mas o mais conhecido deles foi JACK\n\n{jogador.name} fica assustado com aquela informação.\n\n{GREEN+jogador.name+RESET}- JACK? O lendario pirata? aquele que sempre caçava enorme fortunas e ficava conhecido entre todos os sete mares?\n\n{BLUE+'Velho (Jack)'+RESET}- Sim jovem, mas a idade chega para todos...\n\n{GREEN+jogador.name+RESET}- E o que aconteceu com toda a sua fortuna?\n\n{BLUE+'Velho (Jack)'+RESET}- Por volta dos meus 30 anos em minha ultima jornada, finalmente a guarda real conseguiu me encurralar em um estreito canal, perdi tudo o que eu tinha, e a minha tripulação sumiu como poeira no vento.\n\nagora tudo o que me resta são memorias e meu papagaio nesta cabana, mas consigo viver bem, estou muito cansado.\n\n{BLUE+'Velho (Jack)'+RESET}- Escuta 'Viajante', como sabia tudo isso de mim?\n\n{GREEN+jogador.name+RESET}- errr.. quem eu quero enganar.\nCostumava também ser um pirata como o senhor, mas apenas havia eu e meu barco.\nNa minha ultima jornada estava procurando um suposto tesouro em uma pequena ilha proxima ao continente.\nAté uma terrivel tempestade me arrastar para a costa e eu bater o meu barco em um recife de corais.\n\n{BLUE+'Velho (Jack)'+RESET}- Olha só... quem diria..\nAgora deixe eu ver se eu adivinho, voce está andando até a grande cidade do porto para roubar um novo barco certo?\n\n{GREEN+jogador.name+RESET}- Roubar?? hmm não estava nos planos, estou juntando dinheiro no caminho.\n\n{BLUE+'Velho (Jack)'+RESET}- *Solta uma Gargalhada* Que tipo de pirata é esse, eu já me cansei de estar em situações semelhantes a sua, e nunca nem ao menos cogitei juntar moedinhas...\n\n{GREEN+jogador.name+RESET}- hmm e como eu conseguiria roubar um BARCO? a cidade é a mais povoada do reino, existem muitos guardas.\nIsso me parece um plano muito mirabolante, tenho bastante dinheiro acumulado e acredito que conseguiria comprar um barco novo. Sou apenas um caçador de tesouros e não um saqueador.\n\n{BLUE+'Velho (Jack)'+RESET}- Bem meu jovem..., então que assim seja. Mas caso mude de ideia eu já planejei um plano a muito tempo atras quendo eu ainda tinha esperaça...\n\nJack puxa uma rede para {jogador.name} conseguir se deita para dormir...\n\n{BLUE+'Velho (Jack)'+RESET}- Esta quase na minha hora de dormir, então até mais cedo, caso a nossa conversa tenha sido suficiente...",0.01)


    while True:
        textoAnimado('\n\nQual será sua escolha?\n\n1- Perguntar o plano de Jack (Roubar)\n2- Ir dormir\n\nEscolha: ',0.01)
        escolha = (input())
        if escolha == '1':
            textoAnimado(f"\n\n{GREEN+jogador.name+RESET}- Espere!...me diga mais sobre este seu plano.\n\nJack abre um sorriso no canto de sua boca..\n\n{BLUE+'Velho (Jack)'+RESET}- Achei que não iria perguntar.\no plano foi feito a muitos anos, mas acredito aque ainda sirva até os dias atuais. Requer muito cuidado e cautela. \n\n{BLUE+'Velho (Jack)'+RESET}- Primeiro voce terá que ir até o porto e observar a rotina de quem trabalha por lá, desse jeito voce irá descobrir os momentos de menor vigilância.\nDepois disso voce terá que encontrar qual será o barco escolhido, e o restante é sorte meu amigo, más tenho algumas anotações aqui comigo sobre mais alguns passos para voce seguir.",0.01)

            jogador.adicionaItem("Anotações de Jack")
            textoAnimado('\n\nAnotações de Jack adicionadas na mochila',0.01)
            jogador.exibeInventario()

            textoAnimado(f"\n\n{GREEN+jogador.name+RESET}- Entendi, amanhã eu tatarei seguir este plano, obrigado pela dica.\njack vai para o seu quarto e {jogador.name} passa a noite em sua rede improvisada na sala da cabana.\n\nno dia seguinte {jogador.name} acorda bem cedo e a cabana estava vazia.\nComo forma de agradecimento {jogador.name} limpa todo o local e escreve em um pedaço de papel sua gratidão de ter passado uma noite com uma lenda viva, e segue a sua viagem.\ndurante o caminho foi possivel ver Jack bem longe ao rio pescando o seu almoço, mas {jogador.name} estava com pressa e se concentra denovo no seu caminho.\n\n",0.01)
            input('\nDigite para continuar: ')

            Roubo()
            break
        elif escolha == '2':
            textoAnimado(F"\n\n{GREEN+jogador.name+RESET}- O senhor já me ajudou muito, obrigado por tudo! amanhã sairei bem cedo.\n\njack vai para o seu quarto e {jogador.name} passa a noite em sua rede improvisada na sala da cabana.\nno dia seguinte {jogador.name} acorda bem cedo e a cabana estava vazia. Como forma de agradecimento {jogador.name} limpa todo o local e escreve em um pedaço de papel sua gratidão de ter passado uma noite com uma lenda viva, e segue a sua viagem.\n\nDurante o caminho foi possivel ver Jack bem longe ao rio pescando o seu almoço, mas {jogador.name} estava com pressa e se concentra denovo no seu caminho.\n\n",0.01)
            input('\nDigite para continuar: ')

            CidadeDoMar()
            break
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)

def Roubo():
    print("teste")

def CidadeDoMar():
    textoAnimado(f"\nApós caminhar por uma estrada, aos poucos {jogador.name} consegue presenciar o mar aparecendo no horizonte diante dele, e não muito depois uma grandiosa cidade com dezenas de navios atracados em seus portos.\n\nAndando na cidade {jogador.name} nota que nunca esteve em um centro tão grande como aquele, repleto de vendedores de todos os tipos, vários guardas, pessoas andando apressadas pelas ruas e um enorme e imponente Castelo.\n\nBuscando informações sobre como {jogador.name} poderia conseguir um novo barco para sair finalmente do continente, {jogador.name} vai até o porto e percebe que muitos barcos possuiam uma marcação em seus cascos.\n\nPerguntando para um marinheiro {jogador.name} descobre que nesta cidade existe um famoso Artesão responsavel por produzir diversos tipos barcos para vários comerciantes e até mesmo a frota do rei.\n\nCom esta informação {jogador.name} não pensa duas vezes e sai em busca de encontrar o Artesão\n\n\n",0.01)

    textoAnimado(f"Em seu caminho, {jogador.name} observou bem a cidade e andou durante toda aquela manhã sem que nenhuma pista fosse encontrada.\n\nJá quase conformado de que não encontraria o caminho, {jogador.name} para um portuário e faz uma ultima tentativa de perguntar a onde deveria ir.\n\n{GREEN+jogador.name+RESET} - Desculpe-me, senhor, estou à procura de um artesão de barcos renomado nesta cidade.\nSabe onde posso encontrá-lo?\n\n{BLUE+'Portuário'+RESET} - Estou muito ocupado por aqui...\n\n{GREEN+jogador.name+RESET} - Por favor, já estou a manhã toda  procurando!\n\n{BLUE+'Portuário'+RESET} - hmm ta bem, más então me tire uma duvida recente. Voce tem cara de ser bem mais esperto do que eu.\n\n",0.01)

    perguntaCidadeMar.exibirEnunciado()

    while True:
        textoAnimado('Resposta: ',0.01)
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

    perguntaCidadeMar.verificarResposta(resposta)

    
    if perguntaCidadeMar.status == True:
        textoAnimado(f"\n\n{BLUE+'Portuário'+RESET} - Ora como não reparei nisso antes, muito obrigado jovem! O que tinha me perguntado antes mesmo?...\n\n",0.01)
    elif perguntaCidadeMar.status == False:
        textoAnimado(f"\n\n{BLUE+'Portuário'+RESET} - hmm vou procurar um pouco mais sobre... más de qualquer forma obrigado. O que tinha me perguntado antes mesmo?...\n\n",0.01)
    
    textoAnimado(f"{BLUE+'Portuário'+RESET} - Ah sim me lembro, você deve estar falando de Lars, o mestre construtor de barcos.\nEle é um homem notável, e seu estaleiro fica do outro lado do porto, próximo à colina da baía.\nSiga a rua principal até a praça central, e você o encontrará.\n\n{jogador.name} ficou impressionado como a informação estava na ponta de seu nariz o tempo todo, e agradeceu ao portuário com um aceno de cabeça partindo em busca de Lars.",0.01)

    input('\n\nDigite para continuar: ')
    Barco()

def Barco():
    print("teste")

def Resultados():

    print(f"""
            {CYAN+'+---------------------+'+RESET}  
            {CYAN+'|  Reino dos Enigmas  |'+RESET}
            {CYAN+'+---------------------+'+RESET} 

           {CYAN+'- RELATORIO DE QUESTÕES -'+RESET}

        \n\n""")

    perguntaPraia.relatorio()
    perguntaFloresta.relatorio()
    perguntaCaverna.relatorio()
    perguntaFazenda.relatorio()
    perguntaRio.relatorio()
    perguntaCidadeMar.relatorio()
    perguntaBarco.relatorio()

    textoAnimado(f"\n\n{CYAN+f'- QUESTÕES DO ROUBO -'+RESET}",0.01)

    perguntaRoubo1.relatorio()
    perguntaRoubo2.relatorio()
    perguntaRoubo3.relatorio()
    perguntaRoubo4.relatorio()
    perguntaRoubo5.relatorio()



    print(f"""\n\n

           {CYAN+'- PONTOS OBTIDOS -'+RESET}

        \n\n""")

    textoAnimado({CYAN+"Ao longo do jogo foram obtidos:"+RESET},0.01)
    print(f"\n\n {jogador.pontosGeo} {YELLOW+'Pontos na materia Geografia'+RESET}")
    print(f"\n\n {jogador.pontosMat} {YELLOW+'Pontos na materia Matematica'+RESET}")
    print(f"\n\n\n{CYAN+f'O inventario de {jogador.name} possui os itens:'+RESET}")
    jogador.exibeInventario()

    print(f"""\n\n

           {CYAN+'- CONCLUSÃO -'+RESET}

        \n\n""")

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