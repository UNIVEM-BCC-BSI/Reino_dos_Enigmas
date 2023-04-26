import time, sys
def textoAnimado(texto,tempo):
    for i in list(texto):
        print(i, end='')
        sys.stdout.flush()
        time.sleep(tempo)