
VentaData: list = []

class Venta:
    def __init__(self, partido, cliente, asiento, tipo, monto, fecha, iva, id_estadio, id, usada):
        self.partido = partido
        self.cliente = cliente
        self.asiento = asiento 
        self.tipo = tipo
        self.monto = monto
        self.fecha = fecha
        self.iva = iva 
        self.id_estadio = id_estadio
        self.id = id
        self.usada = usada



    def to_pipe(self):
        return self.partido +'|'+self.cliente+'|'+str(self.asiento)+'|'+self.tipo+'|'+str(self.monto)+'|'+str(self.fecha)+'|'+str(self.iva)+'|'+self.id_estadio+'|'+self.id.strip()+'|'+str(self.usada).strip()+"\n"
    
def BuscaVenta(id):
    '''esta funcion busca la venta por id'''
    for item in VentaData:
        if item.id == id:
            return item
    return None 

def Salva(cliente):
    '''esta funcion salva el cliente '''
    VentaData.append(cliente)
    TeamFile = open('VentaData.txt','w')
    for i in VentaData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()
def LoadData():
    '''carga la data'''
    VentaData.clear()
    VentaFile = open("VentaData.txt","r")
    Lines = VentaFile.readlines()

    for line in Lines:
        pp=line.split("|")
        VentaData.append(Venta(pp[0],pp[1],pp[2],pp[3],pp[4],pp[5],pp[6],pp[7],pp[8],pp[9]))
    VentaFile.close()


