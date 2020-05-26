#Verifiar si es un numero primo

Número = int(input("Ingrese un numero mayor que 2: "))
i = 2

while Número % i !=0:
    i += 1
if Número == i:
     print(Número, "No es un número primo")
else:
     print(Número, "Es un número primo")
       