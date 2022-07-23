lista = [1,2,3,4,5]
lista.append(6)     #Agrega un elemento al final de la lista, se puede repetir y con diferentes tipos de valores
print(lista)

lista = [1,2,4,5]
lista.insert(2,3)       #De esta forma se agrega un elemento en la posición que queramos
print(lista)        #Primero se recibe la posición y luego el dato

lista = [1,2,3,4,5]
lista.extend([6,7,8,9,10])      #Sirve para agregar varios elementos de una vez a una lista
print(lista)

lista = [1,2,3,4,5,"Julian"]
print("Julian" in lista)        #De esta forma podemos averiguar si algún elemento pertenece a la lista o no
print(lista.index(5))       #Mostrara a que indice pertenece cierto elemento

print(lista.count(1))       #Nos dice cuantas veces esta ese mismo elemento en la lista

lista = [1,2,3,4,5]
lista.pop()     #Al dejarse sola la función pop eliminara el ultimo elemento
print(lista)

lista = [1,2,3,4,5]
lista.pop(3)        #Así se le indica que elemento eliminar de acuerdo al indice
print(lista)

lista = [1,2,3,4,5]
lista.remove(2)     #De esta forma le estamos diciendo que elimine el elemento que le estamos indicando
print(lista)

lista = [1,2,3,4,5]
lista.clear()       #De esta forma elimina todos los elementos
print(lista)

lista = [1,2,3,4,5]
lista.reverse()     #De esta forma volteamos los elementos de la lista
print(lista)

lista = [1,2,3,4,5]*2       #Así se imprimira 2 veces la lista
print(lista)

lista = [5,4,-7,9,0,1,3]
lista.sort()        #Asi se organizan los elementos de menor a mayor
print(lista)

lista = [5,4,-7,9,0,1,3]
lista.sort(reverse=True)        #Asi se organizan los elementos de mayor a menor
lista[0] = 8        #En los corchetes se ubica el indice y al otro lado del igual el nuevo valor de ese indice
print(lista)