print("**************Tarea 1**************")
age = int(input("Ingresa tu edad:\t"))
if age >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")


print("**************Tarea 2**************")
num = int(input("Ingresa un numero:\t"))
for i in range(num, -1, -1):
    print(i)


print("**************Tarea 2**************")
number = int(input("Ingresa un numero:\t"))
lis = ""
for i in range(0, number, 1):
    lis += "*"
    print(lis)
