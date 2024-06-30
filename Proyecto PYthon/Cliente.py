ClientesData: list = []
class Cliente:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre  
        self.cedula = cedula 
        self.edad = edad 

    def to_pipe(self):
        return self.nombre.strip() +'|'+self.cedula.strip()+'|'+self.edad.strip()+"\n"
    
def BuscaCliente(id):
    for item in ClientesData:
        if item.cedula == id:
            return item
    return None 

def SalvaCliente(cliente):
    ClientesData.append(cliente)
    TeamFile = open('ClientesData.txt','w')
    for i in ClientesData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()

def LoadData():
    ClientesData.clear()
    ClientesFile = open("ClientesData.txt","r")
    Lines = ClientesFile.readlines()

    for line in Lines:
        pp=line.split("|")
        ClientesData.append(Cliente(pp[0],pp[1],pp[2]))
    ClientesFile.close()











