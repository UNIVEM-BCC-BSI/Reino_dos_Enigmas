
class Player():
    def __init__(self, name):
        self.name = name
        self.pontos = 0
        self.pontoMat = 0
        self.pontoGeo = 0
        self.dinheiro = 5
    def daPontoMat(self):
        self.pontoMat += 1
        self.pontos += 1
    def daPontoGeo(self):
        self.pontoGeo += 1
        self.pontos += 1
    def daDinheiro(self, dinheiro):
        self.dinheiro += dinheiro

