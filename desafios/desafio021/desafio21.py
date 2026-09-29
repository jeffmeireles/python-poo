# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa.

from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case "amarelo":
                escolha = "[yellow]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada.")
        else:
            print(f"{self.cor}{msg}[/]", end='')

    def quebrar_linha(self, qtd = 1):
        print("\n" * qtd)

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


c1 = Caneta("Azul")
c2 = Caneta("Vermelho")
c3 = Caneta("Amarelo")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Testando caneta AZUL.")
c1.quebrar_linha(1)
c2.escrever("Testando caneta VERMELHA.")
c2.quebrar_linha(2)
c3.escrever("Testando caneta AMARELA.")
c3.quebrar_linha(3)
