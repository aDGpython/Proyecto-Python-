
EntradaData: list = []
class Entrada:
    def __init__(self, zona, fila, numero, tipo, id_partido, id_estadio):
        self.zona = zona
        self.fila = fila
        self.numero = numero 
        self.tipo = tipo
        self.id_partido = id_partido
        self.id_estadio = id_estadio
    def to_pipe(self):
        return self.zona +'|'+self.fila+'|'+self.numero+'|'+self.tipo+'|'+self.id_partido+'|'+self.id_estadio+"\n"
    
def BuscaEntrada(id):
    for item in EntradaData:
        if item.cedula == id:
            return item
    return None 

def SalvaCliente(cliente):
    EntradaData.append(cliente)
    print(EntradaData)
    TeamFile = open('EntradasData.txt','w')
    for i in EntradaData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()
def LoadData():
    EntradaFile = open("EntradasData.txt","r")
    Lines = EntradaFile.readlines()

    for line in Lines:
        pp=line.split("|")
        EntradaData.append(Entrada(pp[0],pp[1],pp[2],pp[3],pp[4],pp[5]))
    EntradaFile.close()


