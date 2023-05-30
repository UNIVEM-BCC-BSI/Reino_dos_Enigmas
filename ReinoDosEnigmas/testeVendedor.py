from src.Modelo.Perguntas import *
from src.Modelo.Player import *
from src.Config.funcoes import *
from src.Modelo.questoes import *
from src.historia import *


jogador.adicionaItem('rolo de macarrao',5)
jogador.adicionaItem('maça',10)
jogador.adicionaItem('Diamante',3)
jogador.adicionaItem('Paraquedas',30)
jogador.adicionaItem('carteira',1)
jogador.adicionaItem('Moedas de ouro',100)
jogador.adicionaItem('meias',2)

jogador.exibeInventario()

def vendedor(inventario, item, quantidade_item, troca, quantidade_troca):
    if item in inventario:
        quantidade_item_atual = inventario.get(item, 0)
        if quantidade_item_atual >= quantidade_item:
            inventario[item] -= quantidade_item
            inventario[troca] = inventario.get(troca, 0) + quantidade_troca
            print(f"Trocou {quantidade_item} {item} por {quantidade_troca} {troca}.")
        else:
            print("Quantidade insuficiente de itens para a troca.")
    else:
        print("O item não está no inventário.")


# Trocar 1 meia por 100 moedas
vendedor(jogador.inventario, "meias", 1, "Moedas de ouro", 100)

# Exibir inventário atualizado
jogador.exibeInventario()
