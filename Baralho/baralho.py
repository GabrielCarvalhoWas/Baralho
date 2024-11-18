import random
from carta import Carta

class Baralho:
    def __init__(self):
        self.__naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
        self.__valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'As']
        self.__cartas = []
        self.__embaralhado = False

    def criar_baralho(self):
        self.__cartas = [Carta(valor, naipe) for valor in self.__valores for naipe in self.__naipes]

    def embaralhar(self):
        random.shuffle(self.__cartas)
        self.__embaralhado = True

    def distribuir_cartas(self, jogadores):
        for i, carta in enumerate(self.__cartas):
            jogador = jogadores[i % len(jogadores)]
            jogador.adicionar_carta(carta)

    def mostrar_cartas(self):
        return [str(carta) for carta in self.__cartas]
