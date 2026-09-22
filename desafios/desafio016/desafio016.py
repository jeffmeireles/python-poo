 # Crie a classe Funcionário, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar

from rich import print
from rich import inspect

class Funcionario:
    empresa = "LMOL"
    def __init__(self, nome, setor, cargo):
        # Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Olá! Eu me chamo [bold blue]{self.nome}[/] e trabalho no setor de [bold blue]{self.setor}[/] exercendo a função de [bold blue]{self.cargo}[/] na empresa {Funcionario.empresa}:handshake:"

print()
colaborador1 = Funcionario("Jefferson", "E-commerce", "Analista")
print(colaborador1.apresentar())

colaborador2 = Funcionario("Lucas", "Contabilidade", "Analista")
print(colaborador2.apresentar())
print()