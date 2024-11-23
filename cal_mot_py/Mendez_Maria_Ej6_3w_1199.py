print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
#Definir Cadena e los caracteres
def inversa(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida
#El textio va a ser igual a esta aprovado
texto = "estoy probando"
#Invertimos el texto
resultado = inversa(texto)
#Imprim el texto en pantalla
print(f"La inversión de '{texto}' es '{resultado}'")
print(" ")