# Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa
# Considere o consumo padrão de 400g de carne por pessoa e R$82,40/kg de de carne


from rich import print 
from rich.panel import Panel

class Churrasco:
    consumo_padrao:float =  0.400
    preco_kg:float = 82.40
    def __init__(self, titulo, qtd):
        self.titulo = titulo
        self.participantes = qtd

    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} participantes"

    def calcular_qtd_carne(self):
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self):
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando {self.titulo} com {self.participantes} convidados"
        conteudo += f"\nCada participante comerá [green]{Churrasco.consumo_padrao}Kg[/] de carne e cada Kg custa [yellow]R${Churrasco.preco_kg:,.2f}[/]"
        conteudo += f"\nÉ recomendado comprar [green]{self.calcular_qtd_carne()}Kg[/] de carne"
        conteudo += f"\nO valor total do churrasco será de [red]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nE o custo individual será de [yellow]R${self.calcular_custo_individual():,.2f}[/] por pessoa."
        painel = Panel(conteudo, title=self.titulo, width=70)
        print(painel)

c1 = Churrasco("Churras dos Amigos", 20)
c1.analisar()
