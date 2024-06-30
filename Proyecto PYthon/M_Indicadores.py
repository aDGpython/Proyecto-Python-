import Estadio
import Partido
import Producto
import Venta
import VentaRest
import VentaRestProducto
import Cliente

def ordena_valor(diccionario):
  respuesta = sorted(diccionario.items(), key=lambda item: item[1], reverse=True)
  return respuesta


def menu():
    while True: 
        print("\nGestion de partidos y estadios:\n")
        print("1. Promedio de Gasto de un cliente VIP en un partido") 
        print("2. Asistencias a partido")
        print("3. Partido con mayor asistencia")
        print("4. Partido con mayor boletos vendidos")
        print("5. Top 3 productos más vendidos")
        print("6. Top 3 Clientes que compraron más boletos")
        print("0. SALIR")
        x=input("Ingrese el numero de la opcion:  ")
        match x:
            case "1":
                gasto_vip()
            case "2":
                asistencia()
            case "3":
                partido_mayor()
            case "4":
                partido_boletos()
            case "5":
                top_prod()   
            case "6":
                top_clientes()  
            case "0":
                break     
            case _:  
                print("Opcion invalida")

def gasto_vip():
    
    partidos = {}
    for vta in Venta.VentaData:
        if vta.partido.strip() not in partidos:
            partidos[vta.partido.strip()] = 1

    for vta in VentaRest.VentaRestData:
        if vta.partido.strip() not in partidos:
            partidos[vta.partido.strip()] = 1   
    print()
    print("---------------------------------------------------------------------------------------------")
    print("Promedio de gasto cliente VIP")
    print('Partido                                   Promedio')
    for partido in partidos:

        lista = {}
        for vta in Venta.VentaData:
            if vta.partido == partido:
                if vta.cliente not in lista:
                    lista[vta.cliente] = float(vta.monto)
                else:
                    lista[vta.cliente] += float(vta.monto)

        for vta in VentaRest.VentaRestData:
            if vta.partido.strip() == partido:
                if vta.cliente not in lista:
                    lista[vta.cliente] = float(vta.monto)
                else:
                    lista[vta.cliente] += float(vta.monto)
        tot = 0 
        cantidad = 0 
        for cedula,monto in lista.items():
            cantidad += 1 
            tot += float(monto) 
        part = Partido.BuscaPartido(partido)
        nombre= part.fecha+ ' | ' + part.home_team + " vs " + part.away_team
        promedio = float(tot)/float(cantidad)


        print(nombre.ljust(40," "),"%.2f" % round(promedio, 2))
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

def asistencia():
    partidos_a = {}
    partidos_v = {}
    for vta in Venta.VentaData:
        if vta.partido not in partidos_v:
            partidos_v[vta.partido] = 1
            if vta.usada:
                partidos_a[vta.partido] = 1
            else:
                partidos_a[vta.partido] = 0 
        else:
            partidos_v[vta.partido] += 1
            if vta.usada:
                partidos_a[vta.partido] += 1
    ordenados = ordena_valor(partidos_a)
    print()
    print("---------------------------------------------------------------------------------------------")
    print("Info Partido                                                Asistencia  Ventas     Asistencia/Venta")


    for key,val in ordenados:
        part = Partido.BuscaPartido(key)
        estadio = Estadio.BuscaEstadio(part.id_estadio)
        nombre= estadio.nombre_estadio+' | '+part.fecha+ ' | ' + part.home_team + " vs " + part.away_team
        promedio = partidos_a[key]/partidos_v[key]
        
        print(nombre.ljust(65," "),str(partidos_a[key]).ljust(10," "),str(partidos_v[key]).ljust(10," "),"%.2f" % round(promedio, 2))
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

def partido_mayor():
    partidos_a = {}
    for vta in Venta.VentaData:
        if vta.usada:
            if vta.partido not in partidos_a:
                partidos_a[vta.partido] = 1
            else:
                partidos_a[vta.partido] += 1
    ordenados = ordena_valor(partidos_a)
    print()
    print("---------------------------------------------------------------------------------------------")


    print("Info Partido                                               Asistencia   ")

    if len(ordenados) < 1:
        print("No hay asistencias registradas")
        return  
   
    key = ordenados[0][0]
    part = Partido.BuscaPartido(key)
    estadio = Estadio.BuscaEstadio(part.id_estadio)
    nombre= estadio.nombre_estadio+' | '+part.fecha+ ' | ' + part.home_team + " vs " + part.away_team
    
    
    print(nombre.ljust(60," "),str(partidos_a[key]).ljust(10," "))   
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

def partido_boletos():
    partidos_v = {}
    for vta in Venta.VentaData:
        if vta.partido not in partidos_v:
            partidos_v[vta.partido] = 1
        else:
            partidos_v[vta.partido] += 1
    ordenados = ordena_valor(partidos_v)

    print()
    print("---------------------------------------------------------------------------------------------")

    print("Info Partido                                               Ventas   ")
    if len(ordenados) < 1:
        print("No hay partidos vendidos:")
        return

    key = ordenados[0][0]
    # .key()
    part = Partido.BuscaPartido(key)
    estadio = Estadio.BuscaEstadio(part.id_estadio)
    nombre= estadio.nombre_estadio+' | '+part.fecha+ ' | ' + part.home_team + " vs " + part.away_team
    
    
    print(nombre.ljust(60," "),str(partidos_v[key]).ljust(10," ")) 
    print()
    print("---------------------------------------------------------------------------------------------") 
    print() 

def top_prod():
    print()
    print("---------------------------------------------------------------------------------------------")
    print("Top 3 Productos vendidos")



    lista = {}
    for vta in VentaRestProducto.VentaRestProductoData:
        if vta.id_producto not in lista:
            lista[vta.id_producto] = 1
        else:
            lista[vta.id_producto] += 1
    ordenados = ordena_valor(lista)

    if len(ordenados) < 3:
        print("No hay tres productos vendidos!")
        return
    key = ordenados[0][0]
    # .key()
    
    prod = Producto.BuscaProducto(key)
    print("Top 1 ",prod.nombre,prod.id)
    key = ordenados[1][0]
    # .key()
    
    prod = Producto.BuscaProducto(key)
    print("Top 2 ",prod.nombre,prod.id)

    key = ordenados[2][0]
    # .key()
    
    prod = Producto.BuscaProducto(key)
    print("Top 3 ",prod.nombre,prod.id)
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

def top_clientes():
    print()
    print("---------------------------------------------------------------------------------------------")
    print("Top cliente")
    lista = {}
    for vta in Venta.VentaData:
        if vta.cliente not in lista:
            lista[vta.cliente] = float(vta.monto)
        else:
            lista[vta.cliente] += float(vta.monto)
    ordenados = ordena_valor(lista)
    if len(ordenados) < 3:
        print("No hay tres clientes con compra!")
        return
    key = ordenados[0][0]
    # .key()
    
    clie = Cliente.BuscaCliente(key)
    print("Top 1 ",clie.nombre,clie.cedula)
    key = ordenados[1][0]
    # .key()
    
    clie = Cliente.BuscaCliente(key)
    print("Top 2 ",clie.nombre,clie.cedula)

    key = ordenados[2][0]
    # .key()
    
    clie = Cliente.BuscaCliente(key)
    print("Top 3 ",clie.nombre,clie.cedula)
    print()
    print("---------------------------------------------------------------------------------------------")
    print()




