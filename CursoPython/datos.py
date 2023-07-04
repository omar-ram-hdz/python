from tkinter import *
import serial
import os
import threading

carpeta = r"C:\Users\omarr\OneDrive\Documentos\CursoPython"
archivo = r"C:\Users\omarr\OneDrive\Documentos\CursoPython\archivo2.txt"
puerto = "COM"
#-----------------------------

#crear directorio o carpeta si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

if not os.path.exists(carpeta):
    with open(carpeta, "w") as archivo:
        archivo.write("")


#crear puerto serial
try:
    arduino = serial.Serial(puerto, 9600)
except:
    print("No se estableción conexión")


def cerrar_ventana():
    arduino.close()
    root.destroy()

def read_and_save():
    while arduino.is_open:
        #leer datos del puerto serial
        datos = arduino.readline().decode().strip()

        # Mostrar datos en la etiqueta/label
        etiqueta1.config(text=datos)

        #guardar datos en archivo de texto
        with open(carpeta, "a") as archivo:
            archivo.write(datos + "\n")



def iniciar_hilo():
    hilo = threading.Thread(target=read_and_save)
    hilo.daemon = True
    hilo.start()

#----------------------------------------------------------

root = Tk()
root.title("Lectura de Sensor")
root.geometry("400x200")
root.protocol("WM_DELETE_WINDOW", cerrar_ventana)

#crear label/etiqueta para mostrar los datos del sensor
etiqueta1 = Label(root, text="Esperando datos...", font=("Arial", 16))
etiqueta1.grid(row=0, column=0, padx=10, pady=10)

#boton para iniciar la lectura del sensor
boton_start = Button(root, text="Iniciar", font=("Arial", 16), command=iniciar_hilo)
boton_start.grid(row=1, column=0, padx=10, pady=10)

#boton para detener y cerrar ventana
boton_stop = Button(root, text="Cerrar", font=("Arial", 16), command=cerrar_ventana)
boton_stop.grid(row=1, column=0, padx=10, pady=10)

