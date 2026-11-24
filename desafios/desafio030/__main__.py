# Crie uma classe que gerencie a hash SHA256 de uma senha.

from classes030 import Credencial

def main():
    c = Credencial()
    c.senha = input("Digite sua senha: ")
    print(c.senha)

    c.validar('Meireles1234')

if __name__ == "__main__":
    main()