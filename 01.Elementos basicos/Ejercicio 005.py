'''
    Una tienda ofrece un descuento del 15% sobre el total
    de la compra y se desea saber cual es el valor a pagar
    finalmente por la compra
'''
vi = float(input("¿Cual es el valor del producto?: "))
descuento = vi * 0.15
vf = vi - descuento
print(f"El valor total a pagar es: ${vf:.2f}")