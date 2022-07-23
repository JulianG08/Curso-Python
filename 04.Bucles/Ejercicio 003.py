'''
Pide números y mételos en una lista, cuando el usuario
introduzca 0 dejar de insertar y mostrar los números de
menor a mayor
'''

lista = []
salir = False
while not salir:
    num = int(input("Digite un número: "))
    if num==0:
        salir = True
    else:
        lista.append(num)

lista.sort()
print(f"\nLista ordenada : \n{lista}")