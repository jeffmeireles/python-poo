# Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um método que permite mostrar a ficha dessa pessoa

from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()


    def add_favoritos(self, game):
        self.favoritos.append(game)
    

    def mostrar_ficha(self):
        conteudo = f"[blue]Nome real do jogador:[/] {self.nome}"
        conteudo += f"[blue]\nJogos favoritos: [/]"
        for num, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [yellow]{game}[/]'
        ficha = Panel(conteudo, title=f'Jogador: [bold red on white] <{self.nick}> [/]', width=40)
        print(ficha)

jogador1 = Gamer("Jefferson", "MURKRED")
jogador1.add_favoritos("GOD OF WAR")
jogador1.add_favoritos("THE LAST OF US")
jogador1.mostrar_ficha()