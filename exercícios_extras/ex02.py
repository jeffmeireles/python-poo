# EXERCÍCIO 2 — PERSONAGEM DE RPG
# Crie uma classe chamada Personagem.
# A classe deve possuir os seguintes atributos:
# - nome
# - vida
# - ataque
# - defesa
# Crie os seguintes métodos: atacar(outro_personagem), receber_dano(dano), mostrar_status()
# Regras:
# - Quando um personagem atacar outro, o dano causado será: ataque - defesa
# - Caso o resultado seja menor que 0, o dano causado deve ser 0.
# - O personagem não pode atacar se estiver com 0 de vida.
# - A vida nunca pode ficar abaixo de 0.
# - Quando a vida chegar a 0, o personagem está derrotado.

from rich import print
from rich.panel import Panel


class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, outro_personagem):
        if self.vida == 0:
            print('Seu personagem não pode efetuar ataques, pois está com a vida zerada!')
        else:
            dano_recebido = self.ataque - outro_personagem.defesa
            if dano_recebido < 0:
                dano_recebido = 0
            outro_personagem.receber_dano(dano_recebido)
            if outro_personagem.vida == 0:
                painel1 = Panel(f"\n[bold white]O PERSONAGEM {outro_personagem.nome.upper()} FOI [red]DERROTADO![red/][/]\n", title="[red] DERROTADO! [/]", width=41)
                print(painel1)
        
    def receber_dano(self, dano):
        if self.vida - dano < 0:
            self.vida = 0
        else:
            self.vida -= dano
        
    def mostrar_status(self):
        conteudo = f"[bold blue]PERSONAGEM:[/] {self.nome.upper()}"
        conteudo += f"\n[bold blue]VIDA:[/] {self.vida}"
        conteudo += f"\n[bold blue]ATAQUE:[/] {self.ataque}"
        conteudo += f"\n[bold blue]DEFESA:[/] {self.defesa}"
        painel2 = Panel(conteudo, title="[bold black on white] STATUS DO PERSONAGEM [/]", width=40)
        print(painel2)


mago = Personagem("Mago", 100, 200, 15)
cavaleiro = Personagem("Cavaleiro", 160, 30, 20)
mago.atacar(cavaleiro)
cavaleiro.mostrar_status()
mago.mostrar_status()