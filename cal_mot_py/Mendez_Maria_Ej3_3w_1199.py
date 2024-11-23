print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
#Definir insum como a
def isnum(a):
    try:
        int(a)
    except:
        return False;
    return True;
#Definir length como a
def length(a):
    i = 0
#Si a esta en el rango 
    if not (isnum(a)):
        for i in range(len(a)):
            i = i + 1
    elif(isnum(a)):
        return(a)
    return(i)
#Imprime Hola
print(length("hola"))
#Imprime 1, 2, 3, 
print(length(["1","2","3"]))
print(" ")