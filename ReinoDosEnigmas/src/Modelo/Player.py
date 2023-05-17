from src.Config.funcoes import *

class Player:
    def __init__(self, name, item, quantidade=1):
        self.name = name
        self.inventario = {item: quantidade} # Define o item e a quantidade especificada como o valor.
        self.pontosGeo = 0
        self.pontosMat = 0

    def adicionaItem(self, item, quantidade=1):
        if item in self.inventario: # Verifica se o item já está no inventário.
            self.inventario[item] += quantidade # Se o item já existe, incrementa o valor pela quantidade especificada.
        else:
            self.inventario[item] = quantidade # Se o item não existe, cria uma nova chave e define o valor como a quantidade especificada.

    def removeItem(self, item, quantidade=1):
        if item in self.inventario: # Verifica se o item já está no inventário.
            self.inventario[item] -= quantidade # Se o item já existe, diminui o valor pela quantidade especificada.
        else:
            print(RED+f'\n{self.name} não possui o item {item} na mochila.'+RESET) # Se o item não existe, aparece um aviso de erro.

    def exibeInventario(self):
        print(YELLOW+f'\nA mochila de {self.name} atualmente possui:'+RESET)
        print(CYAN+f"{self.inventario}"+RESET)

    def darPontos(self, materia):
        if materia == 'geografia':
            self.pontosGeo += 1
        elif materia == 'matematica':
            self.pontosMat += 1