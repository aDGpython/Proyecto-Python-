
VentaRestProductoData: list = []

class VentaRestProducto:
    def __init__(self, id_restaurante, cliente, tipo, monto, fecha, iva, estadio, id, cantidad, id_producto, id_partido):
        self.id_restaurante = str(id_restaurante)
        self.cliente = cliente
        self.tipo = tipo.strip()
        self.monto = str(monto)
        self.fecha = str(fecha)
        self.iva = str(iva) 
        self.estadio = str(estadio)
        self.id = str(id)
        self.cantidad = str(cantidad)
        self.id_producto = str(id_producto)
        self.id_partido = str(id_partido)
    def to_pipe(self):
        return self.id_restaurante +'|'+self.cliente+'|'+self.tipo+'|'+self.monto+'|'+self.fecha+'|'+self.iva+'|'+self.estadio+'|'+self.id+'|'+self.cantidad+'|'+str(self.id_producto).strip()+'|'+self.id_partido.strip()+"\n"
    
def BuscaVentaRestProducto(id):
    '''Busca la venta de producto en el restaurante con respecto al id'''
    for item in VentaRestProductoData:
        if item.id == id:
            return item
    return None 

def Salva(cliente):
    '''salva el cliente'''
    VentaRestProductoData.append(cliente)
    TeamFile = open('VentaRestProductoData.txt','w')
    for i in VentaRestProductoData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()
def LoadData():
    '''carga la data'''
    VentaRestProductoData.clear()
    VentaRestProductoFile = open("VentaRestProductoData.txt","r")
    Lines = VentaRestProductoFile.readlines()

    for line in Lines:
        pp=line.split("|")
        VentaRestProductoData.append(VentaRestProducto(pp[0],pp[1],pp[2],pp[3],pp[4],pp[5],pp[6],pp[7],pp[8],pp[9],pp[10]))
    VentaRestProductoFile.close()



