
import Cliente
import Partido
import Venta
import Estadio
from datetime import date
import uuid

def es_vampiro(numero):
    if numero <= 0:
        return False    
    digitos = str(numero)
    numero_digitos = len(digitos)
    if numero_digitos % 2 != 0:
        return False
    mitad = numero_digitos // 2
    mitad1 = digitos[:mitad]
    mitad2 = digitos[mitad:]
    num1 = int(mitad1)
    num2 = int(mitad2)
    if num1 * num2 == numero:
        digitos_unicos = set(digitos)
        if len(digitos_unicos) == numero_digitos:
            return True
    return False

def menu():
    print()
    print("---------------------------------------------------------------------------------------------")
    print("Seleccione partido:\n")
    z = 0
    for match in Partido.PartidoData:
        contador = str(z).ljust(3," ")
        match_date = match.fecha.ljust(10," ")
        home_team = match.home_team.ljust(15," ")
        away_team = match.away_team.ljust(15," ")
        print(f"| {contador}| {match_date} | {home_team} vs {away_team} |")
        z += 1 
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
    opcion = input("Seleccione el partido:  ")
    if z >int(opcion):
        partido = Partido.PartidoData[int(opcion)]
        name = partido.fecha+' '+partido.home_team+ ' vs ' +  partido.away_team
        print(f"Partido seleccionado: {name}")
    else:
        print('ERROR de seleccion')
        return
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
    entrada = input("1. Entrada VIP | 75$ |\n2. Entrada general | 35$ |\n")
    if not entrada in "12":
        return 
    stadium = Estadio.BuscaEstadio(partido.id_estadio)
    nombre = stadium.nombre_estadio.ljust(30," ")
    if entrada == "1":
        cantidad = stadium.capacidad_vip
    else:
        cantidad = stadium.capacidad
    print(f"Cantidad de asientos en el estadio {nombre}:  {cantidad}")
    Ocupados = []
    for vta in Venta.VentaData:
        if vta.id_estadio == partido.id_estadio and vta.tipo == entrada:
            Ocupados.append(int(vta.asiento))

    for numero in range(1,int(cantidad)+1):
        if numero in Ocupados:
            print("**** ", end="")
        else:
            print(str(numero).ljust(5," "), end="")  
        if numero % 30 == 0:
            print()
    print()
    asiento = int(input("Ingrese su asiento:  "))
    if asiento > int(cantidad):
        print("Asiento no existe!")
        return
    if asiento in Ocupados:
        print("Asiento ocupado!")
        return
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
    cedulacliente = input("Cedula cliente:  ")
    Customer = Cliente.BuscaCliente(cedulacliente)
    if Customer != None:
        nombrecliente = Customer.nombre
        edad = Customer.edad
        print(f"Cliente existe \nNombre: {nombrecliente}\nEdad: {edad}") 
    else:
        nombrecliente = input("Nombre del cliente:  ")
        edad = input("Edad del cliente:  ") 
        Customer = Cliente.Cliente(nombrecliente,cedulacliente,edad)
        Cliente.SalvaCliente(Customer)
    if entrada == '1': 
        monto = 75
    else:
        monto = 35 
    if es_vampiro(int(cedulacliente)):
        monto /= 2
    iva = monto * .16
    total = monto + iva 
    print(f"monto a pagar: precio: {monto} iva: {iva} total: {total}")
    x= input("1. Pago recibido\n0. Cancelar\n")
    if x == '1':
        uid = str(uuid.uuid1())
        print("Pago registrado")
        venta = Venta.Venta(partido.id_partido,Customer.cedula,asiento,entrada,monto,date.today(),iva,partido.id_estadio,uid,"0")
        Venta.Salva(venta) 
        print(f'El codigo de su boleto es: {uid} Asiento: {asiento} Cliente: {cedulacliente}') 
    print()
    print("---------------------------------------------------------------------------------------------")
    print()