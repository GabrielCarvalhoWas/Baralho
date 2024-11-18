class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor  
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

    def valor_numero(self):  
        valor_mapping = {
            "As": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9,
            "Valete": 10, "Dama": 11, "Rei": 12
        }
        return valor_mapping[self.valor]  
