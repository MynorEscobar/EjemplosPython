texto = input("Ingrese un texto:\t")
decimal = float(input("Ingrese un numero con decimal:\t"))
entero = int(input("ingrese un numero entero:\t"))

print ("Texto: ", texto, "\nDecimal: ", decimal, "\nEntero: ", entero)
print ("Texto: %s \nDecimal %.2f \nEntero: %d" %(texto,decimal,entero))

longitud=len(texto)
print("Longitud: ", longitud)
primerCaracter=texto[0]
print("Primer Caracter: ",primerCaracter) 
segundoCaracter=texto[1]
print("Segundo Caracter: ",segundoCaracter)
ultimoCaracter=texto[-1]
print("Ultimo Caracter: ", ultimoCaracter)
penultimoCaracter=texto[-2]
print("Penultimo Caracter: ", penultimoCaracter)

#texto[posicion inicial, posicion final -1]
subcadena = texto[2:5]
print("del tercer al cuarto caracter: ", subcadena)

subcadena = texto[1:-1]
print("del segundo al penultimo caracter: ", subcadena)

for i in range(len(texto)-1):
    print(texto[i])

for i in range(len(texto)-1,-1,-1):
        print(texto[i])

