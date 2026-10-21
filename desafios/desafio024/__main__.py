# Crie um algoritmo que simule uma cafeteira orientada a objetos.
# O algoritmo deverá ter uma classe mãe chamada BebidaQuente (abstract) que terá os seguintes métodos:
# preparar()
# ferver_agua()
# misturar() (abstract)
# servir() (abstract)
# Devem ser criadas também as seguintes subclasses Cafe, Cha e Leite, que vão herdar os métodos misturar() e servir()

from cafeteira import *

def main():
    bebida1 = Cafe()
    bebida2 = Cha()
    bebida3 = Leite()

    bebida1.preparar()
    bebida2.preparar()
    bebida3.preparar()

if __name__ == "__main__":
    main()