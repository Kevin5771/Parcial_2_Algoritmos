# Desarrolllar un programa que reciba un string en mayusculas o minisculas y retorna la cantidad de 'a' o 'A' 

def preseentación():
    print ("Programa que recibe un string y retorna la cantidad de 'a' o 'A' ")
    print("****************************************************************")

def contador(contador_a):
    cadena = contador_a.lower()
    cantidad = cadena.count("a")
    return cantidad

def cargar():
    texto = input("Ingresa un texto: ")
    cantidad_a = contador(texto)
    print(f"La cantidad de 'a' o 'A' en la cadena es: {cantidad_a}")

#Bloque principal
preseentación()
cargar()


