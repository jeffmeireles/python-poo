from abc import ABC, abstractmethod

class Bebida(ABC):
    def preparar(self):
        print("--- Iniciando o preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida pronta! ---\n")
        
    def ferver_agua(self):
        print("1. Fervendo a água.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(Bebida):
    def misturar(self):
        print("2. Passando água pelo pó de café.")

    def servir(self):
        print("3. Servindo o café em uma xícara.")


class Cha(Bebida):
    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")
    
    def servir(self):
        print("3. Servindo o chá em uma caneca com limão.")


class Leite(Bebida):
    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")
    
    def servir(self):
        print("3. Servindo o leite em uma caneca grande.")