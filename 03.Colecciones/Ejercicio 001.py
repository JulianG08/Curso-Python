'''
    Eliminar elementos repetidos de una lista e imprimirla
'''

lista = [1,2,3,"Julián",2,2,1,"Julián",3]
conjunto = set(lista)
lista = list(conjunto)
print(lista)

lista = list(set(lista))
print(lista)