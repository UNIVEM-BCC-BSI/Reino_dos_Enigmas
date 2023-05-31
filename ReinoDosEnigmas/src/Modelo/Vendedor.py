from src.Config.funcoes import *

class Vendedor:
    def __init__(self, ):
        self.status = False

    def venda(self,inventario, item, quantidade_item, troca, quantidade_troca):

        if item in inventario:
            quantidade_item_atual = inventario.get(item, 0)
            if quantidade_item_atual >= quantidade_item:
                inventario[item] -= quantidade_item
                inventario[troca] = inventario.get(troca, 0) + quantidade_troca
                print(BLUE+F"\n\nForam trocados {quantidade_item} {item} por {quantidade_troca} {troca}."+RESET)
                self.status = True
            else:
                print(RED+f"\n\nQuantidade insuficiente do item {item} para realizar a ação.\n"+RESET)
                self.status = False
        else:
            print(RED+f"O item {item} não está na mochila."+RESET)
            self.status = False
