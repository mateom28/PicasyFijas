from random import randint

nivel = int(input("Ingrese la cantidad de cifras con las que quiere jugar (3,4 o 5 cifras): "))
lista = []
listav = []


def generar_Numero():
    while len(lista) < nivel:
        k = randint(0,9)
        if (k not in lista):
            lista.append(k)
    print (lista)
        
def validar(numero):
    for n in numero:
        if (n not in listav):
            listav.append(n)


def picas_y_fijas():
    f = 0
    p = 0
    x = 0
    for i in lista:
        y = 0
        for j in numero:
            if (lista[x] == numero[y]):
                l = lista[x]
                m = numero[y]
                if (lista.index(l) == numero.index(m)):
                    f = f + 1
                else:
                    p = p + 1
            y = y + 1
        x = x + 1
    print("| Picas || fijas |" + "\n" + "|   "  + str(p) + "   ||   " + str(f) + "   |")  
    if(f == 3):
        print("¡¡FELICITACIONES!!   ¡¡¡¡Ganaste!!!!")

for h in range(15):
    while (nivel < 3 or nivel > 5):
        print("Ingresó número no valido")
        nivel = int(input("Ingrese la cantidad de cifras con las que quiere jugar (3,4 o 5 cifras): "))

    numero = [int(x) for x in input("Ingrese el numero de " + str(nivel) + " cifras: ")]

    while (len(numero) != nivel):
        print("Ingresó número no valido")
        numero = [int(x) for x in input("Ingrese el numero de " + str(nivel) + " cifras: ")]

    validar(numero)

    while (len(listav) < nivel):
        print("No ingrese numeros repetidos") 
        numero = [int(x) for x in input("Ingrese el numero de " + str(nivel) + " cifras: ")]
        validar(numero)

    generar_Numero()
    picas_y_fijas()
    h = h+1
    if h >= 15:
        print("Perdiste!!!")
