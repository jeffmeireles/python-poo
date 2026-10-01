# EXERCÍCIO 3 — PRODUTO E ESTOQUE
# Crie uma classe chamada Produto.
# A classe deve possuir os seguintes atributos: nome, preco e estoque
# Crie os seguintes métodos:
# - adicionar_estoque(quantidade)
# - remover_estoque(quantidade)
# - aplicar_desconto(percentual)
# - mostrar_produto()

# Regras:
# - Não permita adicionar uma quantidade menor ou igual a 0.
# - Não permita remover uma quantidade menor ou igual a 0.
# - Não permita remover uma quantidade maior que o estoque disponível.
# - Não permita aplicar desconto menor que 0%.
# - Não permita aplicar desconto maior que 100%.

from rich import print
from rich.panel import Panel

class Produto:
	def __init__(self, nome, preco, estoque):
		self.nome = nome
		self.preco = preco
		self.estoque = estoque

	def adicionar_estoque(self, qtd):
		if qtd <= 0:
			print("[yellow]Não foi possível atualizar o estoque. Por favor, informe um valor válido.[/]")
		else:
			self.estoque += qtd
			print(f"O estoque do produto {self.nome} foi atualizado com sucesso! [yellow]ADICIONADO {qtd} UNIDADES AO ESTOQUE.[/]")

	def remover_estoque(self, qtd):
		if qtd <= 0:
			print("[yellow]Não foi possível atualizar o estoque. Por favor, informe um valor válido.[/]")
		elif qtd > self.estoque:
			print("[red]O estoque disponível está abaixo da quantidade solicitada[/]")
		else:
			self.estoque -= qtd
			print(f"O estoque do produto {self.nome} foi atualizado com sucesso! [yellow]RETIRADO {qtd} UNIDADES DO ESTOQUE.[/]")

	def aplicar_desconto(self, percentual):
		if percentual < 0 or percentual > 100:
			print("[yellow]Não foi possível aplicar o desconto. Por favor, informe um valor válido.[/]")
		else:
			preco_desconto = self.preco * (percentual / 100)
			self.preco -= preco_desconto

	def disponibilidade(self):
		if self.estoque > 0:
			print(f"O produto {self.nome} está [green]disponível[/] em estoque")
		else:
			print(f"O produto {self.nome} está [red]indisponível[/] no momento")

	def mostrar_produto(self):
		conteudo = f"[blue]PRODUTO:[/] {self.nome.upper()}"
		conteudo += f"\n[blue]PRECO:[/] [green]R${self.preco:.2f}[/]"
		conteudo += f"\n[blue]ESTOQUE DISPONÍVEL:[/] {self.estoque} UNID."
		painel = Panel(conteudo, title="[yellow] STATUS DO ESTOQUE [/]", width=40)
		print()
		print(painel)
		print()


print()

produto1 = Produto("NOTEBOOK", 2500, 30)
produto1.adicionar_estoque(3)
produto1.remover_estoque(50)
produto1.aplicar_desconto(20)
produto1.disponibilidade()
produto1.mostrar_produto()

produto2 = Produto("MOUSE GAMER", 180, 0)
produto2.adicionar_estoque(8)
produto2.remover_estoque(9)
produto2.aplicar_desconto(15)
produto2.disponibilidade()
produto2.mostrar_produto()