import Estadio


'''esta funcion marca y guarda los asientos ya ocupados'''

x = int(input("Cantidad de asientos"))
Ocupados = []
print("catidad de asientos: ",x)
for numero in range(1,x+1):
    if numero in Ocupados:
        print("**** ", end="")
    else:
       print(str(numero).ljust(5," "), end="")  
    if numero % 30 == 0:
        print()
