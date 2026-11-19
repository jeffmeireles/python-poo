from rich import print

class Diario:
    def __init__(self, senha = '@Jlmc12'):
        self.__segredos = []
        self.__senha = senha.strip()


    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())


    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler o meu diário!")
        else:
            print(f"[green]Diário liberado![/]")
            for segredo in self.__segredos:
                print(f"- {segredo}")


    @property
    def senha(self):
        raise PermissionError(f"Ninguém tem permissão para ver a senha")