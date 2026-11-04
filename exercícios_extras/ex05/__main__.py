# EXERCÍCIO 02 - LOCADORA DE VEÍCULOS
# Crie uma classe abstrata Veiculo com:
# - Atributos: marca, modelo, valor_diaria
# - Métodos abstratos: calcular_aluguel(dias), tipo_veiculo()
# - Método concreto: exibir_detalhes()
# Crie três classes filhas:
# - Carro: diária * dias.
# - Moto: desconto de 15% no total.
# - Caminhao: taxa fixa adicional de R$ 200.
# TESTES:
# Crie dois veículos de cada tipo.
# Coloque todos em uma lista e use um único for para exibir os detalhes e o aluguel por 5 dias.

from locadora import *

def main():
    v1 = Carro("Fiat", "Argo", 250)
    v2 = Carro("Volkswagen", "Polo", 350)
    v3 = Moto("Honda", "Fan 160", 55)
    v4 = Moto("Yamaha", "MT-07", 190)
    v5 = Caminhao("Scania", "113", 600)
    v6 = Caminhao("Volvo", "FH 540", 850)

    veiculos = [v1, v2, v3, v4, v5, v6]

    for veiculo in veiculos:
        veiculo.exibir_detalhes(10)

if __name__ == "__main__":
    main()