'''
    Estructura de datos FIFO (first input, first output)
'''

cola = ["Julian","Edison","Edward","Jose","Simon"]
#Agregar elementos al final
cola.append("Mafe")
cola.append("Sofi")
print(cola)
#Sacar elementos por el principio
n = cola.pop(0)
print(f"Atendiendo a {n}")
n = cola.pop(0)
print(f"Atendiendo a {n}")
print(cola)