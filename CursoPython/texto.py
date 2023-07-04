ruta = r"C:\Users\omarr\OneDrive\Documentos\CursoPython\archivo.txt"

#abrir y leer archivos de texto

with open(ruta, "r") as archivo:
    contenido = archivo.read()
    print(contenido)


# sobreescribir archivo de texto
with open(ruta, "w") as archivo:
    archivo.write("Hola de nuevo!")


with open(ruta, "r") as archivo:
    contenido = archivo.read()
    print(contenido)


#para agregar contenido al archivo de texto
with open(ruta, "a") as archivo:
    archivo.write("\nEstoy aprendiendo programación")


with open(ruta, "r") as archivo:
    contenido = archivo.read()
    print(contenido)
