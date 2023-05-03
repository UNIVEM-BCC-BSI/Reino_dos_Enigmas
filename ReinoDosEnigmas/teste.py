from Player import Player
from funcoes import *

BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"



player = str(input('\nNome: '))
playerClass = Player(player)



def caverna():
    textoAnimado(f"\n{playerClass.name} decide ignorar a trilha e se esconder no lugar mais próximo possivel.\nDentro da caverna {playerClass.name} percebe que o ambiente um dia já havia sido uma grande mineração, porém hoje ela estava abandonada e com várias ferramentas antigas e carrinhos cheios de pedra por toda parte.\nExplorando mais o local em busca de uma saida, ao fundo de uma fenda, {playerClass.name} consegue vizualizar uma luz fraca de um lampião.\nChegando mais perto ainda, ele se depara com um Anão com uma enorme barba branca vestindo um macacão sujo e com uma picareta, inpecionando um pequeno cristal tranasparente. {playerClass.name} fica com medo mas percebe que o velho Anão minerador não poderia ser um problema maior do que o Javali do lado de fora da caverna, e resolve ir falar com ele...",0.01)
    textoAnimado(f"\n\n{GREEN+playerClass.name+RESET} - O..Olá?...\n\n O Anão minerador olha para {playerClass.name} e da um pulo de susto...\n\n{BLUE+'Minerador'+RESET} - MEU DEUS!, quem lhe contou que eu estava aqui?? Por acaso te falaram alguma coisa sobre mim???\n\n{GREEN+playerClass.name+RESET} - Não não senhor..., eu só entrei aqui procurando um lugar para me esconder, lá fora tem um Javali que está me perseguindo\n\n{BLUE+'Minerador'+RESET} - Um Javali?, voce entrou nesta antiga mina abandonada só por causa de um Javali?\n\n{GREEN+playerClass.name+RESET} - Sim...\n\n{BLUE+'Minerador'+RESET} - hmm, bem, já que voce está por aqui, finja que nunca me viu, tenho muito trabalho por aqui.\n\n{GREEN+playerClass.name+RESET} - Más o que o senhor está fazendo? preciso de ajuda urgente!, meu tempo é curto e preciso encontrar um local para dormir.\n\n{BLUE+'Minerador'+RESET} - Voce fala demais para o meu gosto eim 'viajante'...\nAposto que foi andado pelos meus irmãos para me vijiar, más como esta caverna não é para amadores como voce, me ajude com uma duvida e eu penso se eu te mostro a saida.\n\n{playerClass.name} fica confuso más aceita o pedido, afinal, não teria como a situação ficar pior.\n\n{GREEN+playerClass.name+RESET} - Ok, eu ajudo.",0.01)

caverna()



#0.08

