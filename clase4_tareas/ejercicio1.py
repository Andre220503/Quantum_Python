#Escribir un programa en python que imprima la lista de números impares hasta el 100 y que imprima cuántos hay.
impares = []
contador = -1
while contador < 99:
    contador = contador + 2
    impares.append(contador)
print(impares)
print(len(impares))