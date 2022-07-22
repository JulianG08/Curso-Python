#Permite construir expresiones logicas, se obtiene como un valor booleano
'''
    Estos son and (conjunción), or (disyunción) y not (negación)
'''
'''
    Para trabajar con and se deben operar 2 valores, ambos deben ser
    verdaderos para ser verdadero

    Para trabajar con or tambien se operan 2 valores pero solo
    uno de ellos debe ser verdadero para tener verdadero

    Not niega el valor que tengamos, si le asignamos un false
    lo convertira en un verdadero y viceversa

    Primero se evalua el not, luego el and y por ultimo el or
'''

a = 10
b = 12
c = 13
d = 10
resultado01 = ((a>b) or (a<c)) and ((a==c) or (a>=b))
print(resultado01)
resultado01 = ((a>b) or (a<c)) and not((a==c) or (a>=b))
print(resultado01)
'''
    La prioridad de los operadores en general tiene el
    siguiente orden
    1. ()
    2. **
    3. *,/,mod,not
    4. +,-,and
    5. >,<,==,>=,<=,!=,or
'''