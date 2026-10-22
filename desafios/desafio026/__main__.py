# Crie uma estrutura capaz de calcular salários de diferentes funcionários .

from calculos import *

def main():
    f1 = FuncionarioMensalista("Jefferson Campos", 2000.00)
    f2 = FuncionarioHorista("Ana Carolina", 25, 240)
    f1.calcular_salario()
    f1.analisar_salario()
    f2.calcular_salario()
    f2.analisar_salario()


if __name__ == "__main__":
    main()