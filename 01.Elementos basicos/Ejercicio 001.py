'''
    Se desea calcular el resultado de una operación
'''
a = float(input("¿Cual es el valor de a?: "))
b = float(input("¿Cual es el valor de b?: "))
c = float(input("¿Cual es el valor de c?: "))
resultado = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"El resultado es: {resultado}")