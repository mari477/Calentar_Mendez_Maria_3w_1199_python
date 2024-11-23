print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ") 
#Definir suma como a
def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i] 
    return total
#Definir multiplicacion como a
def mult(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
#Imprimir la suma y la multiplicacion
print(suma([1,2,3,4]))
print(mult([1,2,3,4]))
print(" ")