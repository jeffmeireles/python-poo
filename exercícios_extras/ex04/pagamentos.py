# Crie uma classe abstrata Pagamento com:
# - Atributo: valor OK
# - Método abstrato: processar() OK
# - Método concreto: exibir_recibo() OK
# Crie três classes filhas:
# - Pix: desconto de 5% no valor. OK
# - CartaoCredito: acréscimo de 8% no valor. OK
# - Boleto: desconto de 2% no valor. OK
# Cada classe deverá implementar processar(), retornando o valor final do pagamento. OK
# TESTES:
# Crie um objeto de cada classe e coloque-os em uma lista. OK
# Use um único for para exibir os recibos. OK
# EXTRA:
# Impeça pagamentos com valores menores ou iguais a zero. OK
# Tente instanciar Pagamento diretamente. OK

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Pagamento(ABC):
    def __init__(self, valor=50):
        self.valor = valor

    @abstractmethod
    def processar(self):
        pass

    def exibir_recibo(self):
        conteudo = f"Subtotal: R$ {self.valor:.2f}"
        conteudo += f"\n[yellow]Total:[/] R$ [green]{self.processar():.2f}[/]"

        recibo = Panel(conteudo, title="[blue]RECIBO DA COMPRA[/]", width=30)
        print(recibo)

class Pix(Pagamento):
    desconto_pix = 5
    def processar(self):
        if self.valor <= 0:
            print("[red]Por favor, informe um valor válido para pagamento![/]")
        return self.valor - (self.valor * Pix.desconto_pix / 100)


class CartaoCredito(Pagamento):
    acrescimo_cartao = 8
    def processar(self):
        if self.valor <= 0:
            print("[red]Por favor, informe um valor válido para pagamento![/]")
        return self.valor + (self.valor * CartaoCredito.acrescimo_cartao / 100)


class Boleto(Pagamento):
    desconto_boleto = 2
    def processar(self):
        if self.valor <= 0:
            print("[red]Por favor, informe um valor válido para pagamento![/]")
        return self.valor - (self.valor * Boleto.desconto_boleto / 100)