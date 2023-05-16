from src.Config.funcoes import *

class Pergunta:
    def __init__(self, enunciado, resposta, alternativa, materia, assunto):
        self.enunciado = enunciado
        self.resposta = resposta
        self.alternativa = alternativa
        self.materia = materia
        self.assunto = assunto

    def exibirEnunciado(self):
        textoAnimado(f'\n{self.enunciado}',0.01)


    def verificarResposta(self, resposta):
        if resposta == self.alternativa:
            self.status = True
        else:
            self.status = False


    def relatorio(self):
        if self.status == True:
            textoAnimado(f"""{YELLOW+'- A resposta que foi dada para a pergunta:'+RESET}

            {self.enunciado}

{YELLOW+f'sobre {CYAN+self.materia+YELLOW} do assunto {CYAN+self.assunto+YELLOW} está correta!'+RESET}\n""",0.01)
        else:
            textoAnimado(f"""{YELLOW+'- A resposta que foi dada para a pergunta:'+RESET}

            {self.enunciado}

{YELLOW+f'sobre {CYAN+self.materia+YELLOW} do assunto {CYAN+self.assunto+YELLOW} está errada!'+RESET}
{YELLOW+f'Resposta correta: {CYAN+self.resposta+YELLOW}'+RESET}\n""",0.01)

# MODO DE UTILIZAÇÃO:

#     *CRIAÇÃO DAS PERGUNTAS

#     questao1 = Pergunta("Qual é a capital do Brasil?\n1- Brasilia\n2- Paris\n3- tocantins", 'Brasilia',"1", "Geografia", "Capitais")
#     questao2 = Pergunta("Qual é a fórmula da água?\n1- skj\n2- h20\n3- url", 'h20',"2", "Química", "Compostos")
#     questao3 = Pergunta("Quem é o autor de Dom Casmurro?\n1- Otávio\n2- pedro\n3- Machado de Assis", 'Machado de Assis',"3", "Literatura", "Autores")

#     *PERGUNTAS INSERIDAS NA HISTORIA

#     questao1.exibirEnunciado()
#     resposta = input("\nResposta: ")
#     questao1.verificarResposta(resposta)

#     questao2.exibirEnunciado()
#     resposta = input("\nResposta: ")
#     questao2.verificarResposta(resposta)

#     questao3.exibirEnunciado()
#     resposta = input("\nResposta: ")
#     questao3.verificarResposta(resposta)

#     *RELATORIO DE RESPOSTAS

#     print("\nRelatório das perguntas:\n")

#     questao1.relatorio()
#     questao2.relatorio()
#     questao3.relatorio()