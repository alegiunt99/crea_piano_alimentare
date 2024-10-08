import cibo

class Verdure(cibo.Cibo):

    def __init__(self,nome, tipologia, quantita, stagione):
        super().__init__(nome, tipologia, quantita)
        self.stagione = stagione
        



    def to_string(self):
        return f"nome: {self.nome}; tipologia: {self.tipologia}, quantita: {self.quantita} g, stagione: {self.stagione}"