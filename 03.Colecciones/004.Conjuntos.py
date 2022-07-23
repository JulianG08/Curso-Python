'''
    Son un tipo de colección donde los datos se agregan de
    forma desordenada donde no pueden haber duplicados

    Se debe agregar la función set al principio para definir
    que estamos haciendo, de no ponerla seria un diccionario

    Dentro de los conjuntos no puede hacer otro tipo de
    colecciones
'''

conjunto = set()
print(conjunto)
conjunto1 = {1, 2, 3, "Hola", 4.56}
print(conjunto1)
conjunto1.add(5)     #Añade elementos
print(conjunto1)
conjunto1.discard(2)     #Borra elementos
print(conjunto1)
print(3 in conjunto1)
print(3 not in conjunto1)
conjunto1.clear()
print(conjunto1)