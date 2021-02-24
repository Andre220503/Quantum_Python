def espacios(lista):
    palabra = ""
    resultado = []
    for i in lista:
        palabra += i
        resultado.append(palabra)
    return resultado

print(espacios(["i","have","no","espace"]))