try:
    divicion = 1 / 0
except ZeroDivisionError:
    print("No es divisible entre cero")
except ValueError:
    print("Tipo de dato incorrecto")
