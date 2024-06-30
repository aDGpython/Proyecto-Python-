
ProductoData: list = []

class Producto:
    def __init__(self, id_restaurante, nombre, precio, inventario, iva, estadio, id, tipo):
        self.id_restaurante = id_restaurante
        self.nombre = nombre
        self.precio = precio
        self.inventario = inventario
        self.iva = iva 
        self.estadio = estadio
        self.id = id
        self.tipo = tipo 

    def to_pipe(self):
        return str(self.id_restaurante) +'|'+self.nombre+'|'+self.precio+'|'+str(self.inventario)+'|'+'0'+'|'+self.estadio+'|'+str(self.id)+'|'+self.tipo.strip()+"\n"
    
def BuscaProducto(id):
    for item in ProductoData:
        if int(item.id) == int(id):
            return item
    return None 

def Salva(nombre):
    ProductoData.append(nombre)
    TeamFile = open('ProductoData.txt','w')
    for i in ProductoData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()


def Guardar():
    file = open('ProductoData.txt','w')
    for i in ProductoData:
        file.write(i.to_pipe())
    file.close()


def LoadData():
    ProductoData.clear()
    ProductoFile = open("ProductoData.txt","r")
    Lines = ProductoFile.readlines()

    for line in Lines:
        pp=line.split("|")
        ProductoData.append(Producto(pp[0],pp[1],pp[2],pp[3],pp[4],pp[5],pp[6],pp[7]))
    ProductoFile.close()



