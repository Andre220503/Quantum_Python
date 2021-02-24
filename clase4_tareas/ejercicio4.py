frase = input("Ingrese la frase: ")
letra_repetida=input("Ingrese la letra: ")
def buscar(frase,repet):
    cont = 0
    for letra in frase:
        if letra == repet:
            cont += 1
    print(f"La letra '{repet}' se repite {cont} veces")
buscar(frase,letra_repetida)