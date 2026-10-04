# Exemplo de Herança em Programação Orientada a Objetos

from rich import inspect

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} acabou de fazer a sua matrícula para o curso {self.curso} na turma {self.turma}.")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} começou a dar aula de {self.especialidade} de nível {self.nivel}")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionário {self.nome} acabou de bater o ponto.")


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