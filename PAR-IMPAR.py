import math

#imput

X= int(input("Digite el valor de x: "))

# processing

r= X%2

if r== 0:
    rta= "PAR"

else:
    rta= "IMPAR"

# output

print("El numero:  " + str(X) + " es " + rta)

    