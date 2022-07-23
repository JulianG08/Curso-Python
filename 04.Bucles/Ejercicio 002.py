

#Agregando elementos a la lista

lista = list(range(1,11))

#Multiplicando los elementos por el valor del usuario

num01 = int(input("Digite un número: "))
for i in lista:
    lista01 = lista * 2
    print(f"Los valores modificados son: {lista01}")