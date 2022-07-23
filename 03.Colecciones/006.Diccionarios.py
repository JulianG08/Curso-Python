'''
    Consisten de clave y valor
'''

diccionario = {}        #Diccionario vacio
print(diccionario)
diccionario = {"azul":"blue","rojo":"red","verde":"green"}
print(diccionario)
print(diccionario["azul"])      #Imprimiendo un elemento determinado
diccionario["amarillo"] = "yellow"      #Agregando nuevos elementos al diccionario
print(diccionario["amarillo"])
del(diccionario["verde"])
print(diccionario)
diccionario = {"Julián":{"edad":18,"estatura":1.60},"Edward":[18,1.62],"Edison":[17,1.68]}
print(diccionario)
print(diccionario["Julián"])