'''
Escriba un programa que tenga dos listas y que a
continuación, cree las siguientes lestas (en las que no debe
haber repeticiones):

 - Lista de elementos que aparecen en las dos listas.
 - Lista de elementos que aparecen en la primera lista, pero no en la segunda.
 - Lista de elementos que aparecen en la segunda lista, pero no en la primera.
 - Lista de elementos que aparecen en ambas listas.
'''

lista01 = [1,2,3,4,5,4,3,2,2,1,5]
lista02 = [4,5,6,7,8,4,5,6,7,7,8]
conjunto01 = set(lista01)
conjunto02 = set(lista02)
a = conjunto01 | conjunto02
b = conjunto01 - conjunto02
c = conjunto02 - conjunto01
d = conjunto01 & conjunto02
lista01 = list(a)
lista02 = list(b)
lista03 = list(c)
lista04 = list(d)
print(f"Los elementos que aparecen en las dos listas son: {lista01}")
print(f"Los elementos que aparecen en la primera pero no en la segunda son: {lista02}")
print(f"Los elementos que aparecen en la segunda pero no en la primera son: {lista03}")
print(f"Los elementos que aparecen en ambas listas son: {lista04}")