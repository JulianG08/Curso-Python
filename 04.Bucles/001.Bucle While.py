'''
    Son bloques de codigo que se repiten una cantidad
    determinada o indeterminada de veces

    El bucle while se le conoce por tener un número
    indeterminado de iteraciones donde se necesita que
    solo una condición se cumpla para ejecutar el bucle
    n veces
'''

import math
num01 = int(input("Digite un número: "))
while num01<0:
    print("Error -> Debe ingresar un número positivo")
    num01 = int(input("Digite un número: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(num01)):.2f}")

i = 0
while i<10:
    print("Hola mundo")
    i += 1