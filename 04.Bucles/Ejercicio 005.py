'''
Hacer un programa para calcular el factorial de un número
positivo
'''

from math import factorial


num = int(input("Digite un número: "))
while num<0:
    print("Error -> El número debe ser positivo")
    num = int(input("Digite un número: "))

#Calcular el factorial
factorial = 1
for i in range(1,num+1):
    factorial *= i

print(f"\nEl factorial del número {num} es {factorial}")