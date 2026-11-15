# Implemente um termostato orientado a objetos.
# Regras:
# A temperatura MÍNIMA é de 16°C
# A temperatura MÁXIMA é de 30°C
# O incremento de temperatura é de 0.5°C a cada vez que girar o termostato

from classes028 import *

def main():
    t = Termostato()
    try:
        t.temperatura = 16.6
    except Exception as e:
        print(f"Houve um problema: {e}")

    print(f"A temperatura atual é de {t.ftemperatura}")
    
if __name__ == "__main__":
    main()