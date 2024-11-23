print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
#Definir la vocal como caracter
def es_vocal(caracter):
    vocales = "aeiouAEIOU"
    return caracter in vocales
#Definir los caracteres con a y b
caracter1 = 'a'
caracter2 = 'b'
#Imprimir si es una vocal
print(f"¿'{caracter1}' es una vocal? {es_vocal(caracter1)}")
print(f"¿'{caracter2}' es una vocal? {es_vocal(caracter2)}")
print(" ")