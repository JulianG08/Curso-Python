#Determinar si dos numeros son pares
num01 = int(input("Digite un número: "))
num02 = int(input("Digite un número: "))
if num01%2==0 and num02%2==0:
    print("Ambos son pares")
elif num01%2==0 and num02%2!=0:
    print(f"{num01} es par")
elif num01%2!=0 and num02%2==0:
    print(f"{num02} es par")
else:
    print("Ambos números son impares")