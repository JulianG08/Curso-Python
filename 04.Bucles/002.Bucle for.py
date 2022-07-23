'''
    Tiene un número determinado de iteraciones, es decir,
    se sabe cuantas veces se va a repetir

    Se usa con colecciones (cualquiera)

    En este caso la variable iteradora recorre la colección
    elemento por elemento
'''

for i in [1,2,3,4,5]:
    print("Hola mundo")

print()

for i in [2,10,3,4,"Julián"]:
    print("Hola todos")

print()

for i in [2,10,3,4,"Julián"]:
    print(f"Elemento : {i}")

print()

coleccion = (4,8,7,3,5)
for i in coleccion:
    print(f"Elemento: {i}")

print()

diccionario = {"Julián":18,"Edison":17}
for i in diccionario:
    print(f"Elemento: {i}")     #Solo toma las claves

print()

for i in diccionario:
    print(f"{diccionario[i]}")      #Imprime los valores

print()

for i in diccionario:
    print(f"{i} -> {diccionario[i]}")       #Imrpime clave y valor

print()

diccionario = {"Julián":18,"Edison":17}
for clave,valor in diccionario.items():
    print(f"{clave} -> {valor}")

print()

'''
    Al aplicarse con una cadena ira caracter por caracter
'''
cadena = "Julián"
for i in cadena:
    print("Hola")
for i in cadena:
    print(f"{i}")
for i in cadena:
    print(f"{i}",end=" ")
for i in cadena:
    print(f"{i}",end="")