#/usr/bin/env python3

#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

#Import library math
import math

cateto_one   = float(input("Enter value cateto one: "))
cateto_two   = float(input("Enter value cateto two: "))
sumcuadrados = cateto_one** 2 + cateto_two** 2
hipotenusa = math.sqrt(sumcuadrados)
print ("The value hipotenusa : ", hipotenusa)


