
"""
    Una lista en Python, es una estructura de datos y tambien es un tipo de dato
    la cual cuenta con características especiales.
    Las listas permiten almacenar cualquier tipo de valor como numeros, textos,
    otras listas.
"""
lista = [1,"hola",[3,"a","b",3,3]]
# las listas inician con el indice 0
print(lista[0])
print(lista[1])
print(lista[2])
print("Primer y segundo elemento: ", lista[0:2])
print("Elemento 2,1 " , lista[2][1])
print("Todos los Elementos: ", lista)

#METODOS
#len: permite obtener la longitud de una lista
print("Longitud: ", len(lista))

#APPEND: Permite agregar un elemento al final de la lista
lista.append("nuevo elemento")
lista.append(10)
print("Lista: ", lista)
print("Nueva longitud: ", len(lista))


#concatenar listas
lista+=[10,20]
print("Lista: ", lista)
print("Nueva longitud: ", len(lista))

#REMOVE: Eliminar un elemento de la lista

print("Nueva Lista xtz: ", lista)


#INSERT: agrega un elemento en indice indicado
lista.insert(0,"Guate")
print("Lista: ", lista)


#INDEX: Devuelve el indice de la primera aparicion del elemento en la lista
print("Indice Elemento 10: " , lista.index(10))
print("Indice Elemento hola: " , lista.index("hola"))

#COUNT: Cuenta las veces que aparece un elemento en la lista
contar = lista.count(10)
print("Elemento 10, cantidad de veces que aparece: ", contar)
contar = lista[3].count(3)
print("Elemento 3, cantidad de veces que aparece: ", contar)

#POP: Elimina el elemento localizado en el indice correspondiente al parametro, al carecer de indice elimina el ultimo elemento
lista.pop(1)
print("POP: Lista: ", lista)

#REMOVE: Elimina el elemento especificado de la lista 
lista.remove("hola")
print("REMOVE Lista: ", lista)

#EXTEND: Extiende una lista agregando un iterable
lista.extend(range(5,8))
print("EXTEND Lista: ", lista)
print("Nueva longitud: ", len(lista))

#REVERSE: coloca los elemento de forma inversa
lista.reverse()
print("REVERSE Lista: ", lista)

#SORT: Ordena los elementos de la lista
lista2=[1,8,3,5,4,1,0]
lista2.sort()
print("Lista: ", lista2)
#El orden en los textos los realiza de forma ascedente acorde al valor en la tabla ascci
lista3=["a","guate","ave","z", "A", "Guate", "Ave", "Z"]
lista3.sort()
print("Lista 3: ", lista3)
lista3=["a","guate","ave","z", "A", "Guate", "Ave", "Z"]

#Ordenar de forma inversa
lista3.sort(reverse=True)
print("Lista 3: Ordenado de forma inversa", lista3)









