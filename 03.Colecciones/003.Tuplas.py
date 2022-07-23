'''
    Son bastante similares a las listas con la particularidad
    de que no pueden ser modificadas
'''

tupla = (4,"Hola",6.78,[1,2,3],4)
print(tupla)
print(tupla[0])
print(tupla[-1])
print(tupla[1:])
print(4 in tupla)
print(tupla.index(4))
print(tupla.count(4))
print(len(tupla))
lista = list(tupla)     #Así se convertiria la tupla en una lista, se puede hacer a la inversa con la función tuple
print(lista)
lista = [1,2,3,4,5]
tupla = tuple(lista)
print(tupla)