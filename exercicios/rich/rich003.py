# Criando tabelas com a biblioteca rich

from rich import print
from rich.table import Table

print()
tabela = Table(title="Tabela de Preços")

tabela.add_column("Produto", justify="left", style="red")
tabela.add_column("Preço", justify="center", style="blue")
tabela.add_row("Lapis", "R$2,00")
tabela.add_row("Borracha", "[yellow]R$3,50[/]")

print(tabela)