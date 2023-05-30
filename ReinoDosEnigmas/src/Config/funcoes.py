import time, sys

RED   = "\033[1;31m"
RESET = "\033[0;0m"
BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"
CYAN  = "\033[1;36m"
YELLOW = "\033[0;33m"

def textoAnimado(texto,tempo):
    for i in list(texto):
        print(i, end='')
        sys.stdout.flush()
        time.sleep(tempo)

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