# EXERCÍCIO 1 — CONTA BANCÁRIA
# Crie uma classe chamada ContaBancaria.
# A classe deve possuir os seguintes atributos:
# - titular
# - numero
# - saldo
# O saldo deve começar em 0 caso nenhum valor seja informado.
# Crie os seguintes métodos:
# - depositar(valor)
# - sacar(valor)
# - mostrar_saldo()
# - mostrar_dados()
# Regras:
# - Não permita depósitos de valores menores ou iguais a 0.
# - Não permita saques de valores menores ou iguais a 0.
# - Não permita sacar um valor maior que o saldo disponível.
# - O método mostrar_saldo() deve mostrar o saldo atual.
# - O método mostrar_dados() deve mostrar o titular, o número
#   da conta e o saldo.
# DESAFIO EXTRA:
# Crie um atributo de classe que registre quantas contas
# foram criadas.

from rich import print
from rich.panel import Panel


class ContaBancaria:
    contas_criadas = 0
    
    def __init__(self, titular, id_conta, saldo=0):
        self.titular = titular
        self.id = id_conta
        self.saldo = saldo
        ContaBancaria.contas_criadas += 1

    def depositar(self, valor):
        if valor <= 0:
            print("\nDEPÓSITO NÃO AUTORIZADO. Por favor, informe um valor válido para depósito.")
        else:
            self.saldo += valor
        
    def sacar(self, valor):
        if valor <= 0:
            print("\nSAQUE NÃO AUTORIZADO. Por favor, informe um valor válido para saque.")
        elif valor > self.saldo:
            print("\nSAQUE NÃO AUTORIZADO POR FALTA DE SALDO.")
        
        else:
            self.saldo -= valor

    def mostrar_saldo(self):
        print(f"\nO SALDO ATUAL DA CONTA Nº[yellow]{self.id}[/] é de [gree]R${self.saldo:.2f}[/]\n")       

    def mostrar_dados(self):
        conteudo = f"[blue]TITULAR DA CONTA:[/] {self.titular.upper()}"
        conteudo += f"\n[blue]ID DA CONTA:[/] {self.id}"
        conteudo += f"\n[blue]SALDO DISPONÍVEL:[/] R${self.saldo:.2f}"
        dados = Panel(conteudo, title=f" [yellow]DADOS DA CONTA {self.id}[/] ", width=40)
        print(dados)

conta1 = ContaBancaria("Jefferson Meireles", 450669, 3800.00)
conta1.depositar(300)
conta1.sacar(100)
conta1.mostrar_saldo()
conta1.mostrar_dados()

conta2 = ContaBancaria("Lucas Campos", 4100, 4800)
conta2.depositar(100)
conta2.sacar(500)
conta2.mostrar_dados()

print(f"CONTAS CADASTRADAS NO SISTEMA: {ContaBancaria.contas_criadas}")