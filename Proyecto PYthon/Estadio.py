EstadioData: list = []

class Estadio:
    def __init__(self, id_estadio, nombre_estadio,capacidad_vip,ciudad,capacidad):
        self.id_estadio = id_estadio
        self.nombre_estadio = nombre_estadio
        self.capacidad_vip = capacidad_vip
        self.ciudad = ciudad
        self.capacidad = capacidad
    def to_pipe(self):
        return self.id_estadio +'|'+self.nombre_estadio+'|'+str(self.capacidad_vip)+'|'+self.ciudad+'|'+str(self.capacidad)+"\n"

    
def BuscaEstadio(id):
    '''esta funcion busca los estadios por id'''
    for item in EstadioData:
        if item.id_estadio == id:
            return item
    return None 

def Salvanombre_estadio(nombre_estadio):
    '''esta funcion salva los nombres de los estadios'''
    EstadioData.append(nombre_estadio)
    print(EstadioData)
    TeamFile = open('EstadioData.txt','w')
    for i in EstadioData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()

def LoadData():
    '''carga la data'''
    EstadioData.clear()
    EstadioFile = open("EstadioData.txt","r")
    Lines = EstadioFile.readlines()

    for line in Lines:
        pp=line.split("|")
        EstadioData.append(Estadio(pp[0],pp[1],pp[2],pp[3],pp[4]))
    EstadioFile.close()




