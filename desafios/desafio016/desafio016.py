 # Crie a classe Funcionário, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar

from rich import print

class Funcionario:
    def __init__(self):
        self.nome = ""
        self.setor = ""
        self.cargo = ""

    def apresentar(self):
        return f"Olá! Eu me chamo {self.nome} e trabalho no setor de {self.setor} exercendo a função de {self.cargo} :handshake:\n"

print()
colaborador1 = Funcionario()
colaborador1.nome = "Jefferson"
colaborador1.setor = "E-commerce"
colaborador1.cargo = "Analista"
print(colaborador1.apresentar())

colaborador2 = Funcionario()
colaborador2.nome = "Lucas"
colaborador2.setor = "Contabilidade"
colaborador2.cargo = "Analista"
print(colaborador2.apresentar())