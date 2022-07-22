#Son de las estructuras más importantes en toda la programación
'''
    Sirven para comparar 2 valores dando como resultado un valor
    logico, verdadero o falso, depende el resultado que se
    obtenga para que se continuen con ciertas acciones
    o no
'''
num = int(input("Digite un número: "))
if num>0:
    print("El número es positivo")
elif num == 0:
    print("El número es cero")
else:
    print("El número es negativo")
print("Fin del programa")