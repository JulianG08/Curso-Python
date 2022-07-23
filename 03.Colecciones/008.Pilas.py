'''
    No existen estructuras de datos directas que las
    utilizen
    (LIFO)last input, first output
'''

pila = [1,2,3]
pila.append(4)
pila.append(5)
print(pila)
#Sacar elementos por el final
n = pila.pop()      #Retorna el elemento afectado
print(f"Sacando el elemento {n}")
print(pila)