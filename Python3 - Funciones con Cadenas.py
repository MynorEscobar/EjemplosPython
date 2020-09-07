texto = input("ingrese un texto: \t")
longitud = len(texto)
print ("Cantidad de caracteres: ", longitud)
pc = texto[0]
print ("Primer caracter: ", pc)
sc = texto[1]
print ("Segundo caracter: ", sc)
uc = texto[-1]
print ("Ultimo caracter: ", uc)
subcadena = texto[-2]
print ("Penultimo caracter: ", subcadena)
subcadena = texto[longitud-1]
print ("Ultimo caracter: ", subcadena)
#texto[posicion inicial: posicion final]
subcadena = texto[0:3]
print("Del primer al tercer caracter", subcadena)
subcadena = texto[4:-3]
print("Del primer caracter al..", subcadena)
for i in range(len(texto)):
    print(texto[i],"\n")

for i in range(len(texto)-1, -1, -1):
    print(texto[i],"\n")







    
