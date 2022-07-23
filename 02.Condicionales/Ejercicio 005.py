'''
    Desarrollado sin bucles
    
    Simular un cajero automático con saldo inicial de $1000
    y contara con el siguiente menú de opciones:

    1. Ingresar dinero en la cuenta
    2. Retirar dinero de la cuenta
    3. Mostrar dinero disponible
    4. Salir
'''

Saldo = 1000
print("\t.:MENU:.")     #Otorga 4 espacios al momento de mostrar el mensaje
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
Opcion = int(input("Digite una opción de menu: "))
print()     #Representa un salto de linea
if Opcion==1:
    extra =float(input("¿Cuanto dinero desea ingresar: "))
    Saldo += extra
    print(f"El dinero disponible es: {Saldo}")
elif Opcion==2:
    retiro =float(input("¿Cuanto dinero desea retirar: "))
    if retiro>Saldo:
        print("Saldo insuficiente")
    else:
        Saldo -= retiro
        print(f"Dinero en la cuenta: {Saldo}")
elif Opcion==3:
    print(f"Dinero en la cuenta: {Saldo}")
elif Opcion==4:
    print("Gracias por utilizar su cajero automático")
else:
    print("Error, se equivocó de opción de menu")