from random import randint

b = open("PicasyFijas.txt", "a")

nombre = input("Ingrese su nombre: ")
nivel = int(input("Ingrese la cantidad de cifras con las que quiere jugar (3,4 o 5 cifras): "))
lista = []
listav = []

b.write("\n" + nombre + ",")
b.write(str(nivel) + ",")

#Genera un número aleatorio
def generar_Numero():
    while len(lista) < nivel:
        k = randint(0,9)
        if (k not in lista):
            lista.append(k)
    print(lista)

#Valida si el número ingresado tiene números repetidos  
def validar(numero):
    for n in numero:
        if (n not in listav):
            listav.append(n)

#Valida cuantas fijas y cuantas picas se hallaron
def picas_y_fijas():
    global f
    global p
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
    b.write(str(p) + "," + str(f) + "," + str(numero) + ",") 


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
    
    if(f == nivel):
        print("¡¡FELICITACIONES!!   ¡¡¡¡Ganaste!!!!")
        b.write(str(h))
        break
    if h > 14:
        print("Perdiste!!!")
        b.write(str(100) + "\n")
b.close()

b = open("PicasyFijas.txt", "r")
ganador = []
for lineas in b.readlines():
    elementos = [str(x) for x in lineas.split(",")]
    if (elementos[1] == str(nivel)):
        c = int(elementos[-1])
        ganador.append(c)
b.close
print(min(ganador))
b = open("PicasyFijas.txt", "r")
for linea in b.readlines():
    elemento = [str(x) for x in linea.split(",")]
    if ((elemento[1] == str(nivel)) and (int(elemento[-1]) == min(ganador))):
        print("El mejor jugador en " + str(nivel) + " cifras, es " + elemento[0] + " con " + elemento[-1] + " intentos") 
b.close()
