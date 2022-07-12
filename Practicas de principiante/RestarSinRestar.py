resta = []

print(""" 

        ---- RESTAR SIN RESTAR ----

""")

valor1 = int(input("Ingrese un valor: "))
valor2 = int(input("Ingrese otro valor: "))

if valor1 == valor2:

    print("El valor es: ",0)

elif valor1 > valor2:

    if valor1 == 0:
        print(valor2)
    
    else:
        for i in range(valor2, valor1):
            
            resta.append(i)

        print("El resultado es: ", len(resta))

else:

    if valor2 == 0:
        print(valor1)

    else:
        for i in range(valor1, valor2):

            resta.append(i)

        print("El resultado es un valor negativo y es: -", len(resta))
        