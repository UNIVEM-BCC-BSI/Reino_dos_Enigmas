from src.Modelo.Perguntas import *
from src.Modelo.Player import *
from src.Config.funcoes import *
from src.Modelo.questoes import *
from src.historia import *



resposta1 = input("resposta: ")
perguntaPraia.verificarResposta(resposta1)
if perguntaPraia.status == True:
    jogador.darPontos("Geografia")

resposta2 = input("resposta: ")
perguntaFloresta.verificarResposta(resposta2)
if perguntaFloresta.status == True:
    jogador.darPontos("Matematica")

resposta3 = input("resposta: ")
perguntaCaverna.verificarResposta(resposta3)
if perguntaCaverna.status == True:
    jogador.darPontos("Geografia")

resposta4 = input("resposta: ")
perguntaFazenda.verificarResposta(resposta4)
if perguntaFazenda.status == True:
    jogador.darPontos("Matematica")

resposta5 = input("resposta: ")
perguntaRio.verificarResposta(resposta5)
if perguntaRio.status == True:
    jogador.darPontos("Geografia")

resposta6 = input("resposta: ")
perguntaCidadeMar.verificarResposta(resposta6)
if perguntaCidadeMar.status == True:
    jogador.darPontos("Geografia")

resposta7 = input("resposta: ")
perguntaBarco.verificarResposta(resposta7)
if perguntaBarco.status == True:
    jogador.darPontos("Matematica")

#  ----------------------------------------------------------------------------------------

resposta8 = input("resposta: ")
perguntaRoubo1.verificarResposta(resposta8)
if perguntaRoubo1.status == True:
    jogador.darPontos("Geografia")

resposta9 = input("resposta: ")
perguntaRoubo2.verificarResposta(resposta9)
if perguntaRoubo2.status == True:
    jogador.darPontos("Geografia")

resposta10 = input("resposta: ")
perguntaRoubo3.verificarResposta(resposta10)
if perguntaRoubo3.status == True:
    jogador.darPontos("Geografia")

resposta11 = input("resposta: ")
perguntaRoubo4.verificarResposta(resposta11)
if perguntaRoubo4.status == True:
    jogador.darPontos("Matematica")

resposta12 = input("resposta: ")
perguntaRoubo5.verificarResposta(resposta12)
if perguntaRoubo5.status == True:
    jogador.darPontos("Matematica")

#=====================================================================================================

def Final():
    print(f"""\n\n


    






                                            {YELLOW+'+---------------------+'+RESET}  
                                            {YELLOW+'|  Reino dos Enigmas  |'+RESET}
                                            {YELLOW+'+---------------------+'+RESET} 



                                            



                        
        
                        
                        """)
    {textoAnimado(BLUE+"- OBRIGADO POR TER JOGADO -"+RESET,0.05)}

                        

    {textoAnimado(CYAN+'\n\n\n\n- CRÉDITOS: -\n\n\n'+RESET,0.05)}

    {textoAnimado("Otávio SBMS\n\nHenry Lacava\n\nJuan Yang\n\nGuilherme Silva\n\nYukio Mawatari\n\n\n\n",0.05)}

    input("Digite para prosseguir: ")
    Resultados()









def Resultados():

    textoAnimado(BLUE+"\n\n\n- RELATÓRIO DE QUESTÕES: -\n\n\n\n\n"+RESET,0.05)

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




    textoAnimado({BLUE+'\n\n\n\n- PONTOS OBTIDOS -\n\n\n\n'+RESET},0.05)


    textoAnimado({CYAN+"Ao longo do jogo foram obtidos:"+RESET},0.01)
    print(f"\n\n {jogador.pontosGeo} {YELLOW+'Pontos na materia Geografia'+RESET}")
    print(f"\n\n {jogador.pontosMat} {YELLOW+'Pontos na materia Matematica'+RESET}")
    print(f"\n\n\n{CYAN+f'O inventario de {jogador.name} possui os itens:'+RESET}")
    jogador.exibeInventario()

    textoAnimado({CYAN+'\n\n\n- CONCLUSÃO -'+RESET},0.05)

    if jogador.pontosGeo < jogador.pontosMat:
        textoAnimado({YELLOW+'\n\nRecomendado maior enfase de estudo na matéria Geografia'+RESET},0.05)
    elif jogador.pontosGeo > jogador.pontosMat:
        textoAnimado({YELLOW+'\n\nRecomendado maior enfase de estudo na matéria Matemática'+RESET},0.05)

    input('\n\n\n\nDigite para sair: ')
    exit()

Final()