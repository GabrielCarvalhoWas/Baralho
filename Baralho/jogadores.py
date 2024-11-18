class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__cartas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def cartas(self):
        return self.__cartas

    def adicionar_carta(self, carta):
        self.__cartas.append(carta)

    def puxar_carta(self):
        if self.__cartas:
            return self.__cartas.pop(0)
        return None

    def tem_cartas(self):
        return len(self.__cartas) > 0

    def mostrar_cartas(self):
        return [str(carta) for carta in self.__cartas]
