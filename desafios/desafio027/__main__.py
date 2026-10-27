# Crie um programa que simule um jogo de RPG onde os personagens possam se curar e atacar uns aos outros.

from personagens import *

def main():
    p1 = Guerreiro("Kratos", 6000)
    p2 = Mago("Sung", 3600)

    p1.atacar(p2, 480)
    p2.atacar(p1, 300)
    p1.curar()
    p2.curar()

if __name__ == "__main__":
    main()