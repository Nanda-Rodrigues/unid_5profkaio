from abc import ABC, abstractmethod

# criamos todas as classes
class CartaoWeb(ABC):
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    @abstractmethod
    def show_message(self):
        pass

class DiaDosNamorados(CartaoWeb):
    def show_message(self):
        print(f"Feliz Dia dos Namorados, {self.destinatario}! Que o amor esteja sempre presente.")

class Natal(CartaoWeb):
    def show_message(self):
        print(f"Feliz Natal, {self.destinatario}! Que sua vida seja cheia de paz, saúde e prosperidade.")

class Aniversario(CartaoWeb):
    def show_message(self):
        print(f"Feliz Aniversário, {self.destinatario}! Muitos anos de vida e felicidades.")

if __name__ == "__main__":
    # Criação das instâncias (todas vistas como "CartaoWeb")
    cartoes = [ DiaDosNamorados("Maria"), Natal("João"), Aniversario("Ana")]

    print("===Comemorações e felicitações===")

    """ POLIMORFISMO:
    todas as variáveis se volta a class do tipo CartaoWeb, e cada objeto chama o método 
    show_message() da sua PRÓPRIA subclasse usando assim, um mesmo método e comportamentos diferentes."""
    for cartao in cartoes:
        cartao.show_message()