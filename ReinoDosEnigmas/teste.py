from Player import Player

BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"



player = str(input('\nNome: '))
playerClass = Player(player)



def cidade():
    print(f"\n\nSeguindo pela floresta {playerClass.name} consegue aos poucos ir percebendo que a vegetação ao seu redor estava mudando, até encontrar uma segunda trilha bem a sua frente, e para a sua surpresa ela aparentava ser bem utilizada.\n Seguindo ela, {playerClass.name} em pouco tempo já se deparava com os enormes muros de uma grande cidade. Adentrando-a, a primeira coisa que chamou a atenção foram os diversos tipos de comerciantes, guardas da cidade e a população reunida em um grande centro com uma praça.\n Desesperado e com medo {playerClass.name} vai atrás de uma ajuda o mais rápido possivel, onde acaba abordando um vendedor em sua barraca de legumes.\n\n {BLUE+'vendedor'+RESET} - Saldações viajante!, o que deseja comprar?\n\n {GREEN+playerClass.name+RESET} - Olá, acabo de chegar nesta cidade e gostaria de saber onde poderia me hospedar.\n\n {BLUE+'vendedor'+RESET} - Ora, a cidade está muito movimentada devido a grandiosa chegada do principe, o filho do rei finalmente retornou depois de uma de suas grandes cavalgadas. Sinto em lhe dizer viajante, más todas as hospedarias da cidade estão ocupadas, a festa será grandiosa!\n\n {GREEN+playerClass.name+RESET} - Não estava sabendo deste evento, estava passando apenas de viagem e iria embora logo ao amanhecer, o senhor conheceria alguem que pudesse me ceder um local para dormir?\n\n o vendedor encara {playerClass.name} da cabeça aos pés...\n\n {BLUE+'vendedor'+RESET} - Bem jovem... estou aqui apenas a trabalho, moro em uma pequena fazenda seguindo ao Norte.\n Entendo a sua situação, um dia eu já fui como voçe, apenas um viajante entre as cidades.\n caso o interesse, o Celeiro de minha fazenda talvez possa te abrigar por hoje.\n\n {GREEN+playerClass.name+RESET} - Claro Senhor! seria um favor enorme...\n")

cidade()