#Llenar una lista con los números del 1 al 50 y mostrarlos

#Agregando los elementos a la lista

lista = list(range(1,51))

#Imprimiendo los elementos de la lista

for i in lista:
    print(f"{i}",end="-")
    if i==49:
        print(50)
        break