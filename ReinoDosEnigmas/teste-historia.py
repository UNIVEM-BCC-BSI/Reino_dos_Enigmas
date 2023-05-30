from src.Modelo.Perguntas import *
from src.Modelo.Player import *
from src.Config.funcoes import *
from src.Modelo.questoes import *
from src.historia import *

jogador.adicionaItem("Moedas de ouro",600)

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

Final()