import Producto
import Restaurante 

def menu():
    '''esta funcion es el menu donde el usuario elige que hacer'''
    while True: 
        print("\nGestion de Restaurantes:\n")
        print("1. Reporte de inventario") 
        print("2. Buscar productos por nombre")
        print("3. Buscar productos por tipo")
        print("4. Buscar producto por rango de precio")
        print("0. SALIR")
        x=input("Ingrese el numero de la opcion:  ")
        match x:
            case "1":
                Reporte_inventario()
            case "2":
                Buscar_Nombre()
            case "3":
                Buscar_Tipo()
            case "4":
                Buscar_Precio()
            case "0":
                break     
            case _:  
                print("Opcion invalida")

def Reporte_inventario():
    '''Esta funcion imprime todos los productos, su inventario y precio'''
    print()
    print("---------------------------------------------------------------------------------------------")   
    print("Reporte de inventario")
    print('Restaurante                             Nombre                             Inventario Precio')

    for prod in Producto.ProductoData:
        rest = Restaurante.BuscaRestaurante(prod.id_restaurante)
        nombre = prod.nombre.ljust(35," ")
        inventario = str(prod.inventario).ljust(10," ")
        price = float(prod.precio)*1.16
        restau = rest.nombre.strip().ljust(40," ")
        print(restau,nombre,inventario,"%.2f" % round(price, 2))
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

def Buscar_Nombre():
    '''esta funcion imrprime el inventraio y precio del producto que el usuario ingreso '''
    print()
    print("---------------------------------------------------------------------------------------------")
    nombre = input("Ingrese el nombre del producto:  ")
    print('Restaurante                             Nombre                             Inventario Precio')
    
    for prod in Producto.ProductoData:
        if prod.nombre == nombre:
            rest = Restaurante.BuscaRestaurante(prod.id_restaurante)
            name = prod.nombre.ljust(30," ")
            inventario = prod.inventario.ljust(10," ")
            price = float(prod.precio)*1.16
            restau = rest.nombre.strip().ljust(40," ")
            print(restau,name,inventario,"%.2f" % round(price, 2))
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

def Buscar_Tipo():
    '''esta funcion imprime el inventario y precio del tipo de producto que el usuario ingreso''' 
    print()
    print("---------------------------------------------------------------------------------------------")
     
    tip = input("Seleccione el tipo del producto:\n 1| Bebidas 2| Comidas 3| Bebidas alcholicas")
    if tip not in ['1','2','3']:
        print("Opcion incorrecta!")
        return 
    if tip == "1":
        tipo = 'non-alcoholic'
    elif tip == "2":
        tipo = "plate"
    else:
        tipo = "alcoholic"
    print('Restaurante                             Nombre                             Inventario Precio')
    for prod in Producto.ProductoData:
        if prod.tipo.strip() == tipo:
            rest = Restaurante.BuscaRestaurante(prod.id_restaurante)
            nombre = prod.nombre.ljust(30," ")
            inventario = prod.inventario.ljust(10," ")
            price = float(prod.precio)*1.16
            restau = rest.nombre.strip().ljust(40," ")
            print(restau,nombre,inventario,"%.2f" % round(price, 2))
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

def Buscar_Precio():
    '''esta funcion busca productos basados en un rango que el usuario ingreso '''
    print()
    print("---------------------------------------------------------------------------------------------")
    print("Productos por rango de precio")


    min = float(input("Ingrese el precio minimo:  "))
    max = float(input("Ingrese el precio maximo:  "))
    print('Nombre                        Inventario Precio  Precio_IVA')
    
    for prod in Producto.ProductoData:

        if float(prod.precio) >= min and float(prod.precio) <= max:

            name = prod.nombre.ljust(30," ")
            inventario = prod.inventario.ljust(10," ")
            price = float(prod.precio)*1.16
            precio = prod.precio.ljust(12," ")

            print(name,inventario,precio,"%.2f" % round(price, 2))
    print()
    print("---------------------------------------------------------------------------------------------")
    print()