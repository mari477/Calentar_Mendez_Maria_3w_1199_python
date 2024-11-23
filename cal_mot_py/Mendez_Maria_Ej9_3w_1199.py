print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
#Definir n como caracter
def generar_n_caracteres(n, caracter):
    resultado = ""
    for _ in range(n):
        resultado += caracter
    return resultado
#Imprimir para generar los caracteres 5 como x
print(generar_n_caracteres(5, "x"))  # Debería devolver "xxxxx"
print(" ")
