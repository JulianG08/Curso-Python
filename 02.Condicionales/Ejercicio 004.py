'''
    Construir una calculadora con las 4 operaciones basicas
    pero el usuario determina cual usar con el primer caracter
    del nombre de la operación

    S, s - Suma
    R, r - Resta
    P, p, M, m - Multiplicación
    D, d - División
'''
num01 = float(input("Digite un número: "))
num02 = float(input("Digite otro número: "))
Operación = input("¿Que operación desea aplicar (solo la inicial): ").lower()
if Operación=='s':
    resultado = num01 + num02
    print(f"El resultado de la operación es: {resultado}")
elif Operación=='r':
    resultado = num01 - num02
    print(f"El resultado de la operación es: {resultado}")
elif Operación=='p' or Operación=='m':
    resultado = num01 * num02
    print(f"El resultado de la operación es: {resultado}")
elif Operación=='d':
    resultado = num01 / num02
    print(f"El resultado de la operación es: {resultado}")
else:
    print("No es una operación valida")