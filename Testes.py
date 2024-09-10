from Moto import Moto
from Veiculo import Veiculo
from Caminhão import Caminhao 
#Instanciando a classe Moto.
Titan160 = Moto("Honda", "Titan 160", "abr-1396", "2005", "160") 
#Exibir uma informação na tela.
#Vai imprimir o retorno do método "__str()__"
print(Titan160.__str__())

chevrolet = Veiculo("Prisma", "Chevrolet", "IZM-9834", 2015)
print(chevrolet.__str__())

scania = Caminhao("Scania", "113H", "IRJ-5987", 2002, 15.575)
print(scania.__str__())
