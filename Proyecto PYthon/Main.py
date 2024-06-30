
import M_Gestion
import M_Ventas
import M_Restaurantes
import M_RestaurantesVenta
import M_Indicadores
import M_Asistencia

def menu():
    '''este es el menu principal donde el usuario elige que hacer'''
    while True:
        print("\nMenu principal:\n")
        print("1. Gestión de partidos y estadios") 
        print("2. Gestión de venta de entradas")
        print("3. Gestión de asistencia a partidos")
        print("4. Gestión de restaurantes")
        print("5. Gestión de venta de restaurantes")
        print("6. Indicadores de gestión (estadísticas)")
        print("0. SALIR")
        x=input("Ingrese el numero de la opcion:  ")
        match x:
            case "1":
                M_Gestion.menu()
            case "2":
                M_Ventas.menu()
            case "4":
                M_Restaurantes.menu()
            case "5":
                M_RestaurantesVenta.menu()
            case "6":
                M_Indicadores.menu()   
            case "3":
                M_Asistencia.menu()       
            case "0":
                break
            case _:  
                print("Valor desconocido")

def cliente():
    print("Datos del cliente\n")
    NameCliente = input("Nombre:  ")
    CedulaCliente = input("Cedula:  ") 
    Edad = input('Edad:  ')   

menu()

