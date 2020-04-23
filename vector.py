import sys
x = float(input("Ingrese el valor de la primera componente del primer vector: "))
y = float(input("Ingrese el valor de la segunda componente del primer vector: "))
z = float(input("Ingrese el valor de la tercera componente del primer vector: "))
"""Ahora debemos ingresar el segundo vector"""
x2 = float(input("Ingrese el valor de la primera componente del segundo vector: "))
y2 = float(input("Ingrese el valor de la segunda componente del segundo vector: "))
z2 = float(input("Ingrese el valor de la tercera componente del segundo vector: "))
print("El vector resultante del producto vectorial es: ")
print((y*z2-z*y2), "i", (z*x2-x*z2), "j", (x*y2-y*x2), "k")
input("Presione cualquier tecla para salir")
sys.exit()

