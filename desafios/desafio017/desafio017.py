# Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto

from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preco = preço

    def etiqueta(self):
        print()
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)
        print()

p1 = Produto("iPhone 17 Pro Max", 5000)
p1.etiqueta()