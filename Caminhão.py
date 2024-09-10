from Veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade = capacidade
    def __str__(self):
        retorno = super().__str__()
        return f'''{retorno}
- Capacidade: {self.__capacidade}'''
    
