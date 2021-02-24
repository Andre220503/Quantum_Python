n = int(input("Introduzca el numero: "))
def multiplo(a, b):
    c = a % b
    if c == 0:
        return True
    else:
        return False
multiplos_3=[]
for i in range(0,n):
    if multiplo(i,3):
        multiplos_3.append(i)
 
print("Los multiplos de 3 hasta el numero ingresado:" , multiplos_3)
