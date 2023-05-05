from src.Config.funcoes import *

while True:
    print(f"""
            {YELLOW+'+---------------------+'+RESET}  
            {YELLOW+'|  Reino dos Enigmas  |'+RESET}
            {YELLOW+'+---------------------+'+RESET} 

            {GREEN+'1 - Iniciar jogo'+RESET}
            {CYAN+'2 - Sobre'+RESET}
            {CYAN+'3 - Créditos'+RESET}
            {CYAN+'4 - Sair'+RESET}
        """)
    textoAnimado('Escolha: ',0.08)
    escolhaInicio = (input())
    if escolhaInicio == '1':
        textoAnimado('\nHavia um pirata solitário chamado', 0.02)
        textoAnimado('... ', 0.5)
        from src.historia import *
        historia()
        break
    elif escolhaInicio == '2':
        print('\nO jogador vivencia um pirata que naufraga em um novo continente e se ve na necessidade de viajar pelas as cidades do Reino dos Enigmas em busca de durante o caminho conseguir lucros para ao final da sua jornada conseguir comprar um novo barco e retornar para a sua casa em um outro reino cruzando o oceano.\nAo longo do caminho podem ser encontrados diversos eventos, como ladrões que podem roubar seu dinheiro, mercados e quests.\nDentro de cada um dos eventos podem ser exibidas perguntas que modificam o cenário de acordo com a resposta do usuário ou modificar o seu inventario.\nAo final da jornada todos os seus itens ou dinheiro obtido será revertido em pontos, e será possivel visualizar um relatório das suas respostas ao longo da jornada, exibindo quais foram as dificuldades do jogador.')
            
        textoAnimado('\nDigite qualquer numero para voltar: ', 0.08)
        (input())

    elif escolhaInicio == '3':
        print("""
            Henry Lacava
            Otávio SBMS
            Juan Yang
            Guilherme Silva
            Yukio Mawatari""")

        textoAnimado('\nDigite qualquer numero para voltar: ', 0.08)
        (input())
            
    elif escolhaInicio == '4':
        print("\nObrigado por jogar!\n")
        quit()

    else:
        print(RED+'\nEscolha uma opção válida.'+RESET)