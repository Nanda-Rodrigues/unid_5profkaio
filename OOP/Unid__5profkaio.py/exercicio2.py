from abc import ABC, abstractmethod

# Classe abstrata
class MetodoPagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def pagar(self):
        pass

class CartaoCredito(MetodoPagamento):# Subclasse - Cartão de Crédito (5% de acréscimo)
    def pagar(self):
        valor_final = self.valor * 1.05
        print(f"Pagamento no Cartão de Crédito. Valor original: R${self.valor:.2f}. "
              f"Com taxa de 5%: R${valor_final:.2f}.")

class BoletoBancario(MetodoPagamento):# Subclasse - Boleto Bancário (2% de desconto)
    def pagar(self):
        valor_final = self.valor * 0.98
        print(f"Pagamento com Boleto Bancário. Valor original: R${self.valor:.2f}. "
              f"Com desconto de 2%: R${valor_final:.2f}.")

class Pix(MetodoPagamento):# Subclasse - Pix (sem alteração)
    def pagar(self):
        print(f"Pagamento via PIX. Valor final: R${self.valor:.2f}.")


# Programa principal
if __name__ == "__main__":

    valor_compra = float(input("Digite o valor da compra: R$ "))

    pagamentos = [CartaoCredito(valor_compra), BoletoBancario(valor_compra), Pix(valor_compra)]

    print("\n=== Simulação dos Métodos de Pagamento ===\n")

    for metodo in pagamentos:
        metodo.pagar()

"""
 Como o uso de polimorfismo facilitou a implementação do sistema de pagamento?

O uso do polimorfismo usou a mesma referencia da lista de pagamento para
diferentes formas de pagamento (CartaoCredito, BoletoBancario, Pix), que 
evitou o uso de vários if/else para verificar o tipo de pagamento e isso
tornou o código mais organizado e fácil de manter:"""

"""
 Quais as vantagens de usar uma interface abstrata nesse contexto?

ela deixa que voce adicione novos codigos ou fucionalidades sem auterar um codigo ja existente
coloca em ordem o comportamento entre os diferentes meios de pagamento e facilita
a substituição e integração de novos métodos de pagamento no sistema, tambem torna o codigo 
mais facil de mater por que nao saõ alteradas as outras classes e podemos reutilizals tambem"""