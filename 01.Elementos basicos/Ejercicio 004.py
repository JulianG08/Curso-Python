'''
    Se quiere averiguar el valor del area y la longitud
    de una circunferencia
'''
import math     #Importa simbolos matematicos
r = float(input("¿Cual es el valor del radio?: "))
area = math.pi * r**2
longitud = 2 * math.pi * r
print(f"El área de la circunferencia es: {area:.2f}\nLa longitud de la circunferencia es: {longitud:.2f}")
#El :.2f limita los decimales a mostrar siendo solo 2 en este caso