import Estadio
import Restaurante
import Producto
import Partido
import Venta
import Cliente
import uuid
import VentaRestProducto
import VentaRest    
from datetime import date

def es_perfecto(numero):
    suma = 0
    for i in range(1,numero):
        if (numero % i == 0):
            suma += i
    print(numero,suma)
    if numero == suma:
        return True
    else:
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
    stadium = Estadio.BuscaEstadio(partido.id_estadio)
    nombre = stadium.nombre_estadio.ljust(30," ")
    cedulacliente = input("Cedula cliente:  ")
    Customer = Cliente.BuscaCliente(cedulacliente)
    if Customer == None:
        print(f"Cliente no existe")
        return
    else:
        print("Nombre: ",Customer.nombre)
        print("Edad: ",Customer.edad)
    si_hay = False
    for vta in Venta.VentaData :
        if vta.partido == partido.id_partido and vta.cliente == cedulacliente and vta.tipo == '1':
            si_hay = True
    if si_hay == False:
        print("No eres VIP!")
        return
    for rest in Restaurante.RestauranteData:
        if rest.id_estadio == partido.id_estadio:
            print(f'{rest.id_restaurante}| Nombre: {rest.nombre.strip()}')
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
            
    selected_restaurant_id = int(input("Ingrese el codigo del restaurante: ")) 
    selected_restaurant = Restaurante.BuscaRestaurante(selected_restaurant_id)     
    if selected_restaurant == None:
        print(f"Restaurante equivocado!")
        return 
    compra = []
    while True:
        print()
        print("---------------------------------------------------------------------------------------------")
        print('Productos del restaurante ', selected_restaurant.nombre)
        print(f'Code Nombre                        Precio     Tipo ')
        for prod in Producto.ProductoData:
            if int(prod.id_restaurante) == selected_restaurant_id:
                
                print(f'{str(prod.id).ljust(4," ")} | {prod.nombre.ljust(30," ")}|{prod.precio.ljust(10, " ")}|{prod.tipo.strip().ljust(10, " ")}')
        print()
        print("---------------------------------------------------------------------------------------------")
        print()        
        selected_producto_id = int(input("Ingrese el número del producto: ")) 
        selected_producto = Producto.BuscaProducto(selected_producto_id)      
        if selected_producto == None:
            print(f"Producto equivocado!")
            continue
        print('Productos seleccionado ', selected_producto.nombre)
        if selected_producto.tipo == "alcoholic" and int(Customer.edad) < 18:
            print("No puedes comprar este producto!")
            continue
        # cantidad = input("Ingrese la cantidad: ")
        print(f"Nombre: {selected_producto.nombre} Precio: {selected_producto.precio} ")
        entrada = input("Seleccione 1 para agregar el producto:  ")
        if  entrada != "1":
            continue
        compra.append(selected_producto.id)
        print(compra)
        entrada = input("seleccione 1 para agregar mas producto, seleccione 0 si quiere terminar la compra:  ")
        if  entrada == "1":
            continue
        uid = str(uuid.uuid1())
        total = 0 
        iva = 0
        print("Factura ", uid)
        for cp in compra:
            selected_producto = Producto.BuscaProducto(cp)
            total += float(selected_producto.precio)
            # iva += float(selected_producto.precio) * 0.16
            vta = VentaRestProducto.VentaRestProducto(selected_restaurant_id,cedulacliente,selected_producto.tipo,selected_producto.precio,date.today(),float(selected_producto.precio)*0.16,partido.id_estadio,uid,'1',selected_producto.id,partido.id_partido)
            VentaRestProducto.Salva(vta)
            print(f"{selected_producto.nombre.ljust(30,' ')}{selected_producto.precio.ljust(12,' ')} ")
            selected_producto.inventario = int(selected_producto.inventario) - 1   
        if es_perfecto(int(cedulacliente)) == True:
            total = total - total*0.15
            print("Su cedula es un numero perfecto, felicidades! Tienes 15% de despuesto")
        iva = float(total) * 0.16 
        Producto.Guardar()
        fac = VentaRest.VentaRest(selected_restaurant_id,cedulacliente,'0',total,date.today(),iva,partido.id_estadio,uid,partido.id_partido)
        VentaRest.Salva(fac)
        print(f'  Total:                          {str(total).ljust(12," ")}')
        print(f'    Iva:                          {str(iva).ljust(12," ")}')
        print(f'  Total a pagar:                  {str(total+iva).ljust(12," ")}')
        print('Factura registrada')
        break
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
        
