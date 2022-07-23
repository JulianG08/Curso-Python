'''
    Son estructuras de datos más flexibles, estas permiten
    almacenar todo tipo de dato, incluyendo otras listas

    Se delimitan por corchetes [] y los elementos se separan
    por comas ,
'''

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
print(lista)

'''
    Empieza a contarse desde el indice 0 hasta el -1
'''

print(lista[0])     #Así se imprimiria un elemento concreto
print(lista[-1])    #Así se va de atras para adelante
print(lista[0:3])   #Así se imprime un rango de elementos, siempre alcanza hasta un elemento a la izquierda
print(lista[:3])    #De esta forma empezara desde el principio
print(lista[1:3])   #Va desde el indice desde el cual le indiquemos
print(lista[2:])    #Va hasta el final

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",40,5.67,[1,2,3],True]
print(lista)
print(len(lista))       #De esta forma podemos saber cuantos elementos tiene la lista