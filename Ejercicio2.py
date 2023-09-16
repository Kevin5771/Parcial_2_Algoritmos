# Desarrollar un Programa las siguiente funciones:
# La Primera que solicite al usuario el ingreso de un valor entero y muestre el cuadrado de dicho valor
# la segunda que solicite la carga de dos valores y muestre el producto de dos mismos.

def Cuadrado():
    print("************************************************")
    valor = int(input("Ingresa un valor entero: "))
    cuadrado = valor ** 2
    print(f"El cuadrado de {valor} es: {cuadrado}")
    print("************************************************")
    print ("    ")


def Producto():
    print("************************************************")
    valor1 = int(input("Ingresa el primer valor: "))
    valor2 = int(input("Ingresa el segundo valor: "))
    producto = valor1 * valor2
    print(f"El producto de {valor1} y {valor2} es: {producto}")
    print("************************************************")

# Bloque Principal

Cuadrado()
Producto()
