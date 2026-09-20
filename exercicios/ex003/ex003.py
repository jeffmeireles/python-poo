# Criando uma conta bancária com POO

def linha(tam = 70):
    print("-" * tam)
    
print()
print("-------- SISTEMA BANCÁRIO --------".center(70))

class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'\nConta {self.id} criada com sucesso! O saldo atual da conta é de R$ {self.saldo:.2f}')

    def __str__(self):
        return f"A conta bancária {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo"

    def depositar(self, valor):
        self.saldo += valor
        linha()
        print(f"\033[32mDEPÓSITO R${valor:.2f} na conta {self.id} autorizado.\033[m")

    def sacar(self, valor):
        if valor > self.saldo:
            linha()
            print(f"\033[31mSAQUE NEGADO!\033[m")
            print(f"Saque no valor de R${valor:.2f} \033[31mNEGADO\033[m por motivos de: \033[33mSALDO INSUFICIENTE\033[m.")
            linha()
        else:
            linha()
            print(f"Saque de R${valor:.2f} da conta {self.id} autorizado.")
            self.saldo -= valor


c1 = ContaBancaria(id=112, nome="Jefferson", saldo=2000)
c1.depositar(1000)
c1.sacar(4000)
print(c1)
print()
