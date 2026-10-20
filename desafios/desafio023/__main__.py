# Crie uma classe abstrata chamada Poligono com:
# - atributo qtd_lados
# - métodos abstratos perimetro() e area()
# Crie as classes Quadrado e Circulo que herde de Poligono: perimetro() e area()
# Utilize ABC e abstractmethod.
# TESTE:
# Crie um Quadrado e um Circulo e exiba seus atributos,
# perímetros e áreas.
# DESAFIO:
# Crie uma função que receba um Poligono e exiba seu perímetro e sua área, testando com Quadrado e Circulo.

from poligono import Quadrado, Circulo

def main():
    quadrado = Quadrado(20)
    print(f"Um quadrado de lado {quadrado.lado}cm tem perímetro de {quadrado.perimetro()} cm")
    print(f"Um quadrado de lado {quadrado.lado}cm tem área de {quadrado.area()} cm2")

    circulo = Circulo(15)
    print(f"Um círculo de raio {circulo.raio} cm tem perímetro de {circulo.perimetro():.1f}cm")
    print(f"Um círculo de raio {circulo.raio} cm em área de {circulo.area():.1f} cm2")


if __name__ == "__main__":
    main()