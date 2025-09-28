class Veiculo:
    total_veiculos = 0

    def __init__(self, placa, modelo, diaria):
        self.__placa = placa
        self.modelo = modelo
        self.diaria = diaria
        self.__alugado = False
        Veiculo.total_veiculos += 1

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, value):
        print("A placa não pode ser modificada.")
    
    def alugar(self):
        if not self.__alugado:
            self.__alugado = True
            print(f"Veículo {self.modelo} alugado com sucesso!")
        else:
            print(f"Veículo {self.modelo} já está alugado.")

    def devolver(self):
        if self.__alugado:
            self.__alugado = False
            print(f"Veículo {self.modelo} devolvido com sucesso!")
        else:
            print(f"Veículo {self.modelo} já está disponível.")

    def status(self):
        if self.__alugado:
            return f"Veículo {self.modelo} está alugado."
        else:
            return f"Veículo {self.modelo} está disponível."

    @classmethod
    def mostrar_total_veiculos(cls):
        print(f"Total de veículos cadastrados: {cls.total_veiculos}")

    @staticmethod
    def calcular_preco(diaria, dias):
        return diaria * dias

def main():
    veiculos = [
        Veiculo("ABC1234", "Classic", 150),
        Veiculo("DEF5678", "Cadete", 120),
        Veiculo("GHI9012", "Fox", 200)
    ]

    print("Veículos disponíveis:")
    for i, veiculo in enumerate(veiculos):
        print(f"{i+1}. {veiculo.modelo} - Placa: {veiculo.placa}")

    try:
        escolha = int(input("Escolha o veículo que deseja gerenciar (digite o número): ")) - 1
        if escolha >= 0 and escolha < len(veiculos):
            veiculo_escolhido = veiculos[escolha]
            while True:
                print("\nOpções:")
                print("1. Alugar veículo")
                print("2. Devolver veículo")
                print("3. Ver status do veículo")
                print("4. Calcular preço do aluguel")
                print("5. Voltar ao menu principal")
                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    veiculo_escolhido.alugar()
                elif opcao == "2":
                    veiculo_escolhido.devolver()
                elif opcao == "3":
                    print(veiculo_escolhido.status())
                elif opcao == "4":
                    dias = int(input("Digite o número de dias: "))
                    preco = Veiculo.calcular_preco(veiculo_escolhido.diaria, dias)
                    print(f"Preço do aluguel: R${preco}")
                elif opcao == "5":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print("Veículo não encontrado.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()
