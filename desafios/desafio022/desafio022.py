# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples (canal, volume e liga/desliga)

from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_min = 1
    canal_max = 5
    volume_min = 1
    volume_max = 10

    def __init__(self,  canal = 1, volume = 2):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def mostrar_tv(self):
        conteudo = ""
        if not self.ligado:
            conteudo = f":prohibited:[red] A TV está desligada.[/]"
        else:
            conteudo = f"Canal = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += "[white on yellow] [/]"
                else:
                    conteudo += f" {canal} "

            conteudo += "\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan] [/]"
                else:
                    conteudo += "[black on white] [/]"
        tv = Panel(conteudo, title=" [TV] ", width= 30)
        print(tv)


c = ControleRemoto()
while True:
    c.mostrar_tv()
    comando = input(" < CH >        - VOL + ")
    match comando:
        case "0":
            break
        case ">":
            c.canal_mais()
        case "<":
            c.canal_menos()
        case "+":
            c.volume_mais()
        case "-":
            c.volume_menos()
        case "@":
            c.liga_desliga()
    print("\n" * 10)
