PI = 3.1416


# Funcion circulo
def areaCirculo(date: float, type_: str):
    if type_ == "radio":
        return (PI * date) ** 2
    if type_ == "diametro":
        return (PI * (date * 2)) ** 2


# Funcion lista
def promedio(array: list):
    if len(array) <= 1:
        return "Necesitas mas de 2 numeros"
    for i in array:
        if type(i) != int and type(i) != float:
            return "Los datos no coinciden con el tipo de dato que es float"
    suma = 0
    for i in array:
        suma += i
    return suma / len(array)


#                            AREA CIRCULO
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
result = areaCirculo(
    float(input("Ingresa el radio o el diametro: \t")),
    input("Ingresa que es, 'radio' o 'diametro' :\t"),
)


print("{}".format(result))


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Promedio lista
lista = []
aux = ""
while True:
    aux = input("Ingresa un numero: \t")
    try:
        try:
            aux = int(aux)
        except:
            aux = float(aux)
    except:
        print("Error, vuelve a ingresar")
        continue

    lista.append(aux)
    if input("¿Deseas continuar? Si/no \t") in ["si", "Si", "SI", "sI", "S"]:
        continue
    else:
        break

print("El promedio es: {}".format(promedio(lista)))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
