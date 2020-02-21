#/usr/bin/env python3

cantidadNumeros = input("Digite cantidad de datos: ")
numeros = list(map(int, input("Datos de entrada").split()))

total = 0 
lenNumeros = len(numeros)
print("cantidadNumeros", cantidadNumeros)
print("count numeros", lenNumeros)
if int(cantidadNumeros) == lenNumeros:
    for x in numeros: 
        total += x 
    print("la suma es ", total)
else:
    print("La cantidad de números debe ser igual a la cantidad de datos")
