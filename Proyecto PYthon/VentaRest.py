
VentaRestData: list = []

class VentaRest:
    def __init__(self, id_restaurante, cliente, tipo, monto, fecha, iva, estadio, id, partido):
        self.id_restaurante = str(id_restaurante)
        self.cliente = cliente
        self.tipo = tipo
        self.monto = str(monto)
        self.fecha = str(fecha)
        self.iva = str(iva )
        self.estadio = str(estadio)
        self.id = str(id)
        self.partido = str(partido)

    def to_pipe(self):
        return self.id_restaurante +'|'+self.cliente+'|'+self.tipo+'|'+str(self.monto)+'|'+self.fecha+'|'+self.iva+'|'+self.estadio+'|'+self.id.strip()+'|'+self.partido.strip()+"\n"
    
def BuscaVentaRest(id):
    '''Busca la venta con respecto al id'''
    for item in VentaRestData:
        if item.id == id:
            return item
    return None 

def Salva(cliente):
    '''Salva el cliente'''
    VentaRestData.append(cliente)
    TeamFile = open('VentaRestData.txt','w')
    for i in VentaRestData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()
def LoadData():
    '''carga la data'''
    VentaRestData.clear()
    VentaRestFile = open("VentaRestData.txt","r")
    Lines = VentaRestFile.readlines()

    for line in Lines:
        pp=line.split("|")
        VentaRestData.append(VentaRest(pp[0],pp[1],pp[2],pp[3],pp[4],pp[5],pp[6],pp[7],pp[8]))
    VentaRestFile.close()



