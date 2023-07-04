from tkinter import *

raiz = Tk()

raiz.title("Ejemplo de GUI")
raiz.resizable(1,1) #1=> ancho 2 => alto
#1=> redi 0 => no 
raiz.geometry("800x400")
raiz.config(bg="black")

cuadro = Frame()
cuadro.pack(fill="x",expand="True",side = "top")
cuadro.config(bg="white",width="600",height="300",bd="10",cursor="cross")
raiz.mainloop()

""" 
1: funcion del area de un circulo
2: Media de varios numeros
"""