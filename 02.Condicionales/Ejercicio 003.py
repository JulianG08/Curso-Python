'''
    Determinar si el caracter que nos brinda el usuario es
    una vocal o no
'''
caracter = input("Digite un caracter: ").lower()        #De esta forma se convierte en minuscula
if caracter=='a' or caracter=='e' or caracter=='i' or caracter=='o' or caracter=='u':
    print("Es una vocal")
else:
    print("No es una vocal")