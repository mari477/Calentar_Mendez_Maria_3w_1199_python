print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
#Definir variable de palindromo como cadena
def es_palindromo(cadena):
#Convertimos la cadena a minúsculas y eliminamos espacios
    cadena = cadena.replace(" ", "").lower()
#Comparamos la cadena con su inversa
    return cadena == cadena[::-1]
#Imprimimos helloo, hola y Hola como estan todos
print(es_palindromo("helloo"))  # Debería devolver True
print(es_palindromo("hola"))   # Debería devolver False
print(es_palindromo("Hola como estan todos"))  # Debería devolver True
print(" ")