
EquipoData: list = []

class Equipo:
    def __init__(self, id_equipo, nombre, codigo, grupo):
        self.id_equipo = id_equipo
        self.nombre = nombre
        self.codigo = codigo
        self.grupo = grupo
    def to_pipe(self):
        return self.id_equipo +'|'+self.nombre+'|'+self.codigo+'|'+self.grupo+"\n"
    
def BuscaEquipo(id):
    '''esta funcion busca los equipos por id'''
    for item in EquipoData:
        if item.id == id:
            return item
    return None 

def Salvanombre(nombre):
    '''esta funcion salva los nombres de los equipos'''
    EquipoData.append(nombre)
    print(EquipoData)
    TeamFile = open('EquipoData.txt','w')
    for i in EquipoData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()
def LoadData():
    '''carga la data'''
    EquipoData.clear()
    EquipoFile = open("EquipoData.txt","r")
    Lines = EquipoFile.readlines()

    for line in Lines:
        pp=line.split("|")
        EquipoData.append(Equipo(pp[0],pp[1],pp[2],pp[3]))
    EquipoFile.close()



