print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
#creamos las funsiones que son a, b y c
def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
#ejecutamos con los numeros que ya pusimos que van a ser 10, 20, 15
numero1 = 10
numero2 = 20
numero3 = 15
#Resultado del maximo de los tres numeros
resultado = max_de_tres(numero1, numero2, numero3)
#Imprimo el resultado
print(f"El número mayor entre {numero1}, {numero2} y {numero3} es {resultado}")
print(" ")
