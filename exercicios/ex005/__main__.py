# O exercício 005 organiza o exercício 004 em módulos para deixar o programa mais limpo e organizado.

from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

a1 = Aluno("Jefferson", 23, "ADS", 1002)
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1)

p1 = Professor("João", 45, "Biologia", "superior")
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1)

f1 = Funcionario("Lucas", 30, "Analista", "E-commerce")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1)