valor=int(input("ingrese un numero:\t"))
residuo=0
contar=0
#llegar hasta el valor ingresado
for i in range(1, valor+1):
  residuo=valor%i
  if(residuo==0):
    contar+=1
if(contar>2):
  print(valor," no es primo")
else:
  print(valor, " es un primo")


