import time
from jogadores import Jogador
from baralho import Baralho
from carta import Carta

class Batalha:
    def __init__(self, jogadores):
        self.jogadores = jogadores

    def realizar_batalha(self):
        jogador1, jogador2 = self.jogadores
        carta1 = jogador1.puxar_carta()  
        carta2 = jogador2.puxar_carta()  

        if carta1 and carta2:
            print(f"Jogador1: {jogador1.nome} puxou: {carta1}")
            print(f"Jogador2: {jogador2.nome} puxou: {carta2}")

            if carta1.valor_numero() > carta2.valor_numero():
                print(f"{jogador1.nome} vence a batalha!")
                jogador1.adicionar_carta(carta1)  
                jogador1.adicionar_carta(carta2)  
            elif carta2.valor_numero() > carta1.valor_numero():
                print(f"{jogador2.nome} vence a batalha!")
                jogador2.adicionar_carta(carta1) 
                jogador2.adicionar_carta(carta2)  
            else:
                print("Empate! As cartas são devolvidas.")
                jogador1.adicionar_carta(carta1)  
                jogador2.adicionar_carta(carta2)  

        else:
            print("Um dos jogadores não tem cartas suficientes!")


class Jogo:
    def __init__(self, nomes_jogadores):
        self.jogadores = [Jogador(nome) for nome in nomes_jogadores]
        self.baralho = Baralho()
        self.batalha = Batalha(self.jogadores)
        self.rodadas = 0

    def iniciar(self):
        self.baralho.criar_baralho()
        self.baralho.embaralhar()
        self.baralho.distribuir_cartas(self.jogadores)

    def mostrar_status(self):
        for jogador in self.jogadores:
            print(f"{jogador.nome} tem {len(jogador.cartas)} cartas!")

    def jogo_terminado(self):
        return any(not jogador.tem_cartas() for jogador in self.jogadores)

    def executar(self):
        self.iniciar()


        while self.rodadas < 8 and not self.jogo_terminado():
            print(f"Rodada {self.rodadas + 1}")
            self.batalha.realizar_batalha()
            self.mostrar_status()
            self.rodadas += 1

        if self.rodadas >= 8:
            print("\nEsperando o restante da batalha . . . . .")
            time.sleep(3)  

    
        for jogador in self.jogadores:
            if jogador.tem_cartas():
                print(f"{jogador.nome} venceu o jogo!")
                break
        else:
            print("O jogo terminou em empate!")

if __name__ == "__main__":
    nomes = input("Digite o nome do jogador 1: "), input("Digite o nome do jogador 2: ")
    jogo = Jogo(nomes)
    jogo.executar()
