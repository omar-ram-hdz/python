print("Promedio")
name = input("ingresa tu nombre: ")
fisica = float(input(name + " ¿Cual es tu calificacion de fisica?"))
quimica = float(input(name + " ¿Cual es tu calificacion de quimica?"))
mate = float(input(name + " ¿Cual es tu calificacion de matematicas?"))
espaniol = float(input(name + " ¿Cual es tu calificacion de español?"))
promedio = (fisica + mate + quimica + espaniol) / 4
# print("Tu promedio es:", round(promedio, 1))
# round() reduce el numero de decimales, p1 = nombre de la variable, p2 = numero de decimales


if promedio >= 6:
    print("Aprobaste")
elif promedio == 10: #como else if
    print("Excelente calificacion")
else:
    print("Reprobaste")
