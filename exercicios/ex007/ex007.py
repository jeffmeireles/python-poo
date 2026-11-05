class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f'\nConta {self.id} criada com sucesso! O saldo atual da conta é de R$ {self.__saldo:.2f}')

    def __str__(self):
        return f"A conta bancária {self.id} de {self._titular} tem R${self.__saldo:.2f} de saldo"

    def depositar(self, valor):
        self.__saldo += valor
        print(f"\033[32mDEPÓSITO R${valor:.2f} na conta {self.id} autorizado.\033[m")

    def sacar(self, valor):
        if valor > self.__saldo:
            print(f"\033[31mSAQUE NEGADO!\033[m")
            print(f"Saque no valor de R${valor:.2f} \033[31mNEGADO\033[m por motivos de: \033[33mSALDO INSUFICIENTE\033[m.")
        else:
            print(f"Saque de R${valor:.2f} da conta {self.id} autorizado.")
            self.__saldo -= valor