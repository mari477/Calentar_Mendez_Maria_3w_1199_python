print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
#DEfinir la lista 1 y la lista 2
def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
#Lista a, b, c. son igual a los numeros 1,2,3,4,5,6,3,8,7,9 y 10
lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 3, 8]
lista_c = [7, 9, 10]
print(superposicion(lista_a, lista_b))  #devolver True (tienen el 3 en común)
print(superposicion(lista_a, lista_c))  #devolver False (no tienen elementos en común)
print(" ")
