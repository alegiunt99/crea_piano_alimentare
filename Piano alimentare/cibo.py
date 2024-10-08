class Cibo:
    
    def __init__(self,nome, tipologia, quantita):
        self.nome = nome
        self.tipologia = tipologia
        self.quantita = quantita


    
    def to_string(self):
        return f"nome: {self.nome}; tipologia: {self.tipologia}, quantita: {self.quantita} g"


