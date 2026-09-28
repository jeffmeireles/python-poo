# Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.

from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_de_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você abriu o livro '[red]{self.titulo}[/]' que tem [green]{self.total_de_paginas} páginas[/]. Você está na [yellow]página {self.pagina_atual}[/][blue/]")


    def avancar_pagina(self, qtd=1):
        cont = 0
        for pg in range (0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Página {self.pagina_atual} :arrow_forward: ", end='')
                sleep(0.7)
                cont += 1
        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][blue/]")

        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou no final do livro '{self.titulo}'[/]")


    def fim_do_livro(self):
        if self.pagina_atual == self.total_de_paginas:
            return True
        else:
            return False


l1 = Livro("Fogo e Sangue", 580)
l1.avancar_pagina(5)