# Simule um diário secreto orientado a objetos.
# Regra: qualquer um pode escrever nesse diário, mas lê-lo só será possível se souber a senha.

from diario import *

def main():
    d = Diario()
    d.escrever("Primeira mensagem do diário.")
    d.escrever("Segunda mensagem de teste.")
    try:
        d.ler("@Jlmc12")
    except Exception as e:
        print(f"[red]ERRO: {e}")


if __name__ == "__main__":
    main()