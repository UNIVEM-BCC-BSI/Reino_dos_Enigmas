from src.Modelo.Perguntas import *
from src.Modelo.Player import *
from src.Modelo.Vendedor import *
from src.Config.funcoes import *
from src.Modelo.questoes import *
from src.historia import *

jogador.adicionaItem("Moedas de ouro",1)
jogador.adicionaItem("Pedra Brilhante",2)
jogador.adicionaItem("Conchinhas",2)
jogador.adicionaItem("Trufas negras",2)
jogador.adicionaItem("chupeta",2)

def CidadeDoMar():
    textoAnimado(f"\nApós caminhar por uma estrada, aos poucos {jogador.name} consegue presenciar o mar aparecendo no horizonte diante dele, e não muito depois uma grandiosa cidade com dezenas de navios atracados em seus portos.\n\nAndando na cidade {jogador.name} nota que nunca esteve em um centro tão grande como aquele, repleto de vendedores de todos os tipos, vários guardas, pessoas andando apressadas pelas ruas e um enorme e imponente Castelo.",0.01)

    while True:
        textoAnimado('\nQual será sua escolha?\n\n1 - Entrar em uma loja \n2 - Continuar andando\n\n\n',0.01)
        escolhaParte2 = input("Escolha: ")
        if escolhaParte2 == '1':
            comerciante = Vendedor()
            textoAnimado(f"\nEm meio a toda a agitação, uma loja com a fachada repleta de coisas empilhadas chama a atenção de {jogador.name},\n\nque decide conhecer o lugar mais de perto...\n\n\n{BLUE+'Comerciante'+RESET} - Olá meu amigo!, venha venha entre!\n\n\n{jogador.name} começa a andar em meio a caixas repletas de bugingangas e velharias espalhadas\n\n\n{BLUE+'Comerciante'+RESET} - O que temos para mim hoje??\n\n{GREEN+jogador.name+RESET} - Para voce?\n\n{BLUE+'Comerciante'+RESET} - Claro amigo, o que podemos negociar??\n\n\n{jogador.name} percebe naquele instante que o estranho lugar se tratava de uma loja de penhores.\n\n\n{GREEN+jogador.name+RESET} - hmm acho que tenho algumas coisas por aqui...\n\n\n",0.01)

            print("\n\ndeseja vender algo?\n\n1- sim\n\n2- não\n")
            while True:
                textoAnimado('Resposta: ',0.01)
                escolha = (input())
                if escolha == '1':
                    
                    
                    jogador.exibeInventario()

                    while True:

                        x = input(YELLOW+"\n\nDigite qual item de sua mochila deseja vender, Para parar, digite 'fim': "+RESET)

                        if x == "fim":
                            textoAnimado(f"\n\n{GREEN+jogador.name+RESET} - Isto é tudo no momento,\n acho que já vou indo\n\n{BLUE+'Comerciante'+RESET} - Até mais amigo!, te espero aqui!\n\n\nSaindo da loja {jogador.name} continua a sua missão.\n\n\n",0.01)
                            CidadeDoMarPt2()
                            break

                        elif x in jogador.inventario:
                            if x == "Pedra Brilhante":
                                comerciante.venda(jogador.inventario,"Pedra Brilhante",1,"Moedas de ouro",100)
                                jogador.exibeInventario()
                            elif x == "Conchinhas":
                                comerciante.venda(jogador.inventario,"Conchinhas",1,"Moedas de ouro",15)
                                jogador.exibeInventario()
                            elif x == "Trufas negras":
                                comerciante.venda(jogador.inventario,"Trufas negras",1,"Moedas de ouro",50)
                                jogador.exibeInventario()
                            else:
                                textoAnimado(f"\n\n{BLUE+'Comerciante'+RESET} - Infelizmente não aceito este tipo de mercadoria...\n\n",0.01)
                        else:
                            print(RED+f"O item {x} não existe em sua mochila."+RESET)


                elif escolha == '2':    
                    textoAnimado(f"\n\n{GREEN+jogador.name+RESET} - No momento não tenho interesse senhor, estava apenas observando a sua loja,\n más acho que já vou indo\n\n{BLUE+'Comerciante'+RESET} - Até mais amigo!, te espero aqui!\n\n\nSaindo da loja {jogador.name} continua a sua missão.\n\n\n",0.01)
                    CidadeDoMarPt2()
                    break
                else:
                    print(RED+'\nEscolha uma opção válida.'+RESET)
            
            
        elif escolhaParte2 == '2':
            CidadeDoMarPt2()
            
        else:
            print(RED+'\nEscolha uma opção válida.'+RESET)

CidadeDoMar()