'''
    Hacer un programa para determinar que número es mayor
'''
num01 = int(input("Digita un número: "))
num02 = int(input("Digita un número: "))
num03 = int(input("Digita un número: "))
if num01>=num02 and num01>=num03:
    print(f"El número {num01} es mayor")
elif num02>=num01 and num02>=num03:
    print(f"El número {num02} es mayor")
elif num03>=num01 and num03>=num02:
    print(f"El número {num03} es mayor")