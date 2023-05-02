import time, sys


RED   = "\033[1;31m"
RESET = "\033[0;0m"
BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"
CYAN  = "\033[1;36m"


def textoAnimado(texto,tempo):
    for i in list(texto):
        print(i, end='')
        sys.stdout.flush()
        time.sleep(tempo)