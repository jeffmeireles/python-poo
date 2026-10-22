# Crie classes capazes de calcular fretes de diferentes veículos (moto, caminhão e drone).
# Moto: fator 0.50 | Frete mínimo - livre
# Caminhão: fator - 1.20 | Frete mínimo - 50Km
# Drone: fator - 9.50 | Frete máximo - 10Km

from transportadora import *
from rich import print, inspect
from rich.table import Table


def main():
    dist = 50

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for item in viagem:
        tabela.add_row(f"{dist}Km", f"{type(item).__name__}", f"{item.calcular_frete()}")

    print(tabela)

if __name__ == "__main__":
    main()