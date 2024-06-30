
RestauranteData: list = []

class Restaurante:
    def __init__(self, id_restaurante, id_estadio, nombre):
        self.id_restaurante = id_restaurante
        self.id_estadio = id_estadio
        self.nombre = nombre
    def to_pipe(self):
        return str(self.id_restaurante) +'|'+self.id_estadio+'|'+self.nombre+"\n"
    
def BuscaRestaurante(id):
    for item in RestauranteData:
        if int(item.id_restaurante) == int(id):
            return item
    return None 

def Salva(id_estadio):
    RestauranteData.append(id_estadio)
    TeamFile = open('RestauranteData.txt','w')
    for i in RestauranteData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()
def LoadData():
    RestauranteData.clear()
    RestauranteFile = open("RestauranteData.txt","r")
    Lines = RestauranteFile.readlines()

    for line in Lines:
        pp=line.split("|")
        RestauranteData.append(Restaurante(pp[0],pp[1],pp[2]))
    RestauranteFile.close()



