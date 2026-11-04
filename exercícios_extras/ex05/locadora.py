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

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Veiculo(ABC):
    def __init__(self, marca, modelo, valor_diaria):
        self.marca = marca
        self.modelo = modelo
        self.valor_diaria = valor_diaria

    @abstractmethod
    def calcular_aluguel(self, dias):
        pass

    @abstractmethod
    def tipo_veiculo(self):
        pass

    def exibir_detalhes(self, dias):
        conteudo = f"TIPO DE VEÍCULO ALUGADO: [yellow]{self.tipo_veiculo()}[/]"
        conteudo += f"\nMARCA: {self.marca}"
        conteudo += f"\nMODELO: {self.modelo}"
        conteudo += f"\nDIÁRIA: {self.valor_diaria}"
        conteudo += f"\nDIAS: {dias}"
        conteudo += f"\nTOTAL: R$ [yellow]{self.calcular_aluguel(dias):.2f}[/]"
        detalhes = Panel(conteudo, title="[blue]Detalhes da Locação[/]", width=40)
        print(detalhes)


class Carro(Veiculo):
    def calcular_aluguel(self, dias):
        return self.valor_diaria * dias

    def tipo_veiculo(self):
        return "Carro"


class Moto(Veiculo):
    def calcular_aluguel(self, dias):
        desconto = 15
        valor_total = self.valor_diaria * dias
        valor_com_desc = valor_total - (valor_total * desconto / 100)
        return valor_com_desc

    def tipo_veiculo(self):
        return "Moto"

class Caminhao(Veiculo):
    def calcular_aluguel(self, dias):
        return self.valor_diaria * dias + 200

    def tipo_veiculo(self):
        return "Caminhão"