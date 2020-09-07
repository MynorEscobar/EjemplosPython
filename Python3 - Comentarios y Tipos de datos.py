#Comentarios y tipos de datos

#comentario de linea
"""
comentario de bloque, es decir,
varias lineas

"""
numero = 10
texto = "Texto"
numeroDecimal = 15.25
logico = True
logio2 = False

print ("\n\n")
print ("""Una tupla es una secuencia ordenada de items inmutables,
        los elementos pueden ser de distinto tipo""") 
tupla=(10,20,30,"Fin")
print ("Tupla: " , tupla)
print ("Tupla, elemento primer elemento: " , tupla[0])
print ("Tupla, tercer elemento: " , tupla[3])
print ("Tupla, penultimo elemento: ", tupla[-2])
print ("\n\n\"hola\"")
print ("""Una lista es una secuencia ordenada de elementos mutable,
        los elementos pueden ser de distinto tipo""") 
lista=[10,20,30,"Fin"]
print ("Lista: " , lista)
print ("Lista, elemento primer elemento: " , lista[0])
print ("Lista, tercer elemento: " , lista[3])
print ("Lista, penultimo elemento: ", lista[-2])
print ("Lista, ultimo elemento: ", lista[-1])
print ("Lista, rango de elementos: ", lista[1:3])

lista[1] = 200
print ("Lista modificada: ", lista)

print("\n\n")
print("Diccionario: un diccionario es una colección no-ordenada de valores que son accedidos a traves de una clave.")
diccionario = dict()

diccionario = {
    1: "Uno",
    2: "Dos",
    3: "Tres",
    "cuatro": "Ultimo elemento"
}
print("Diccionario: ", diccionario)
print("Diccionario, primer elemento: ", diccionario.get(3))
print("Diccionario, ultimo elemento: ", diccionario.get("cuatro"))


















