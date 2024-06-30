import Venta
# Esta funcion valida la entrada que ingresa el usuario
def valida():
    entrada = input("Ingrese el codigo de su entrada:")
    encontrada = False
    for vta in Venta.VentaData:

        if vta.id == entrada:
            print("Validado")
            vta.usada = 1 
            File = open('VentaData.txt','w')
            for i in Venta.VentaData:
                File.write(i.to_pipe())
            File.close()
            encontrada = True 
    if encontrada == False:
        print('boleto no encontrado!')
        return
    else:
        print("boleto encontrado")
        







def menu():
    while True: 
        print("\nGestion de boleto:\n")
        print("1. Ingresar al partido") 
        print("0. SALIR")
        x=input("Ingrese el numero de la opcion:  ")
        match x:
            case "1":
                valida()
            case "0":
                break     
            case _:  
                print("Opcion invalida")