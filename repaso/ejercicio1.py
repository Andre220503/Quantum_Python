numeros_turco = {
 0 : "sifir",
 1 : "bir", 
 2 : "iki", 
 4 : "dört",
 5 : "beş",
 6 : "altı",
 7 : "yedi",
 8 : "sekiz",
 9 : "dokuz"}
decenas_turco = {
    10 : "on",
    20 : "yirmi",
    30 : "otuz",
    40 : "kirk",
    50 : "elli",
    60 : "altmış",
    70 : "yetmiş",
    80 : "seksen",
    90 : "doksan"
} 

valor = int(input("Introduzca un numero del 1 al 99: "))
def turco(a):
    if len(str(valor)) == 1:
        a = numeros_turco.get(valor)
        print(f"{valor} es {a}")
    if len(str(valor)) == 2:
        a = decenas_turco.get(valor)
        print(f"{valor} es {a}")
    if len(str()        
turco(valor)
