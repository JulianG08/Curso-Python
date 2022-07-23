'''
    Pueden usarse en cualquiera de los bucles

    Al usarse el continue se obvia lo que sigue en las
    instrucciones

    El break rompe la ejecución del bucle
'''

for i in range(10):
    print(i)

print()

for i in range(10):
    if i==5:
        continue
    print(i)

print()

for i in range(10):
    if i==5:
        break
    print(i)

print("Programa finalizado")