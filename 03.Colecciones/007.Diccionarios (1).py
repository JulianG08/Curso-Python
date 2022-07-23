equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Critiano Ronaldo",17:"Mario Mandzukic"}
print(equipo)
print(equipo[10])
#print(equipo[6])        #Representa un keyerror ya que no se encuentra en el diccionario
print(equipo.get(17,"No existe un jugador con ese dorsal"))
print(equipo.get(9,"No existe un jugador con ese dorsal"))
print(10 in equipo)
print(12 in equipo)
print(equipo.keys())        #Solo imprime las claves
print(equipo.values())      #Solo imprime los valores
print(equipo.items())       #Imprime los elementos agrupados por tuplas
print(len(equipo))      #Permite saber el número de elementos del diccionario
equipo.clear()      #Borra todos los elementos
print(equipo)