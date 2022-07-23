'''
    El set solo es necesario cuando se va a crear un
    conjunto vacio
'''
a = {1,2,3}
b = {3,4,5}
print(a == b)
b = {3,1,2}
print(a == b)
print(len(a))
b = {3,4,5}
c = a | b       #Unión de conjuntos
print(c)
c = a & b       #Intersección de conjuntos
print(c)
c = a - b       #Diferencia de conjuntos
print(c)
c = a ^ b       #Diferencia simetrica de conjuntos
print(c)
c = {1,2,3,4,5}
print(a.issubset(c))        #Saber si un conjunto es subconjunto de otro
print(b.issubset(c))
print(c.issuperset(a))      #Saber si un conjunto contiene a otro
print(a.isdisjoint(b))      #Saber si no tienen elementos en común
'''
    Con la función "frozenset()" podemos hacer inmutable
    el conjunto deseado
    a = frozenset({1,2,3})
'''