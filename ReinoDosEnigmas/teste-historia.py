from src.Modelo.Perguntas import *
from src.Modelo.Player import *
from src.Config.funcoes import *
from src.Modelo.questoes import *
from src.historia import *

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

Resultados()