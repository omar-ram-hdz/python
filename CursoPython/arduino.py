from tkinter import *
from time import sleep
import serial

try:
    arduino = Serial("COM3", 9600)
except:
    print("No hubo conexion")


sleep(1)


def pressOn1():
    textDescription1.configure(
        text="Encendido",
        fg="green",
    )
    arduino.write("1\n")


def pressOff1():
    textDescription1.configure(
        text="Apagado",
        fg="red",
    )
    arduino.write("1\n")


def pressOn2():
    textDescription2.configure(
        text="Encendido",
        fg="green",
    )
    arduino.write("2\n")


def pressOff2():
    textDescription2.configure(
        text="Apagado",
        fg="red",
    )
    arduino.write("2\n")


def pressOn3():
    textDescription3.configure(
        text="Encendido",
        fg="green",
    )
    arduino.write("3\n")


def pressOff3():
    textDescription3.configure(
        text="Apagado",
        fg="red",
    )
    arduino.write("3\n")


def closeWin():
    if arduino.close():
        win.destroy()
    else:
        win.destroy()


win = Tk()
win.protocol("WM_DELETE_WINDOW", closeWin)
win.geometry("500x500")
win.title("Arduino - Python")

btnEncenderLed1 = Button(
    win,
    text="LED off",
    command=pressOff1,
    padx=10,
    pady=10,
    width=10,
)
btnEncenderLed1.grid(
    row=0,
    column=0,
)
btnApagarLed1 = Button(
    win,
    text="LED1 on",
    command=pressOn1,
    padx=10,
    pady=10,
    width=10,
)
btnApagarLed1.grid(
    row=0,
    column=1,
)
textDescription1 = Label(
    win,
    fg="red",
    text="Apagado",
    font=("Arial", 14),
    padx=10,
    pady=10,
)
textDescription1.grid(
    row=0,
    column=2,
)


btnEncenderLed2 = Button(
    win,
    text="LED off",
    command=pressOff2,
    padx=10,
    pady=10,
    width=10,
)
btnEncenderLed2.grid(
    row=1,
    column=0,
)
btnApagarLed2 = Button(
    win,
    text="LED1 on",
    command=pressOn2,
    padx=10,
    pady=10,
    width=10,
)
btnApagarLed2.grid(
    row=1,
    column=1,
)
textDescription2 = Label(
    win,
    fg="red",
    text="Apagado",
    font=("Arial", 14),
    padx=10,
    pady=10,
)
textDescription2.grid(
    row=1,
    column=2,
)


btnEncenderLed3 = Button(
    win,
    text="LED off",
    command=pressOff3,
    padx=10,
    pady=10,
    width=10,
)
btnEncenderLed3.grid(
    row=2,
    column=0,
)
btnApagarLed3 = Button(
    win,
    text="LED1 on",
    command=pressOn3,
    padx=10,
    pady=10,
    width=10,
)
btnApagarLed3.grid(
    row=2,
    column=1,
)
textDescription3 = Label(
    win,
    fg="red",
    text="Apagado",
    font=("Arial", 14),
    padx=10,
    pady=10,
)
textDescription3.grid(
    row=2,
    column=2,
)


btnExit = Button(
    win,
    text="Cerrar",
    padx=10,
    pady=10,
    command=closeWin,
)
btnExit.grid(
    row=3,
    column=1,
)
win.mainloop()

# alt control shift r
