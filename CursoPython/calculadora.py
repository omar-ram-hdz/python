from math import sqrt

bol = True


while bol:
    print(
        "Menu\n Selecciona una de las opciones \n 1.Suma\n 2.Resta \n 3.Multiplicacion \n 4.Divicion \n 5.Raiz cuadrada\n 6.Salir\n \t"
    )
    option = int(input(""))
    if option == 1 or option == 2 or option == 3 or option == 4:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
    if option == 1:
        print("El resultado de la suma es:", num1 + num2)
    elif option == 2:
        print("El resultado  de la resta es:", num1 - num2)
    elif option == 3:
        print("El resultado de la multiplicacion es:", num1 * num2)
    elif option == 4:
        print("El resultado de la divicion es:", num1 / num2)
    elif option == 5:
        num = int(input("Ingresa un numero"))
        print("La raiz cuadrada del numero es:", sqrt(num))
    elif option == 6:
        bol = False
    else:
        print("Opcion incorrecta, intentalo denuevo \n \n")

# Potencia numero ** 2  Numero al cuadrado
#pow() numero, raiz 1/2 = cuadrada 1/3 cubica
print("Fin del programa")
