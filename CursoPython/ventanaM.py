from tkinter import *


def multiplicacion():
    text3.configure(state="normal")
    if not text1.get() and not text2.get():
        stringOut = "No ingresaste ningun numero"
        text3.delete(0, "end")
        text3.insert(0, stringOut)
    else:
        if not text1.get():
            num1 = 1
        else:
            num1 = int(text1.get())
        if not text2.get():
            num2 = 1
        else:
            num2 = int(text2.get())
        stringOut = "{}".format((num1 * num2))
        text3.delete(0, "end")
        text3.insert(0, stringOut)
    text3.configure(state="readonly")


def clear():
    text3.configure(state="normal")
    text1.delete(0, "end")
    text2.delete(0, "end")
    text3.delete(0, "end")
    text3.configure(state="readonly")


def close():
    root.destroy()


root = Tk()
root.title("Programa multiplicacion")
root.geometry("500x230")
root.configure(bg="#222222")

label1 = Label(
    root,
    text="Primer numero:",
    bg="#222222",
    font=("Arial", 14),
    fg="#f7df1e",
)  # etiqueta
label1.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
)
label2 = Label(
    root,
    bg="#222222",
    text="Segundo numero:",
    font=("Arial", 14),
    fg="#f7df1e",
)
label2.grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
)

label3 = Label(
    root,
    text="Resultado:",
    bg="#222222",
    fg="#f7df1e",
    font=("Arial", 14),
)
label3.grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
)


text1 = Entry(root)
text1.place(
    x=50,
    y=50,
)
text1.grid(
    row=0,
    column=1,
    padx=5,
    pady=5,
)
text1.configure(
    foreground="#222222",
    highlightcolor="#f7df1e",
    highlightbackground="#222222",
    highlightthickness=2.5,
    bg="white",
)


text2 = Entry(root)
text2.place(
    x=50,
    y=50,
)
text2.grid(
    row=1,
    column=1,
    padx=5,
    pady=5,
)
text2.configure(
    foreground="#222222",
    highlightcolor="#f7df1e",
    highlightbackground="#222222",
    highlightthickness=2.5,
    bg="white",
)


text3 = Entry(root)
text3.place(
    x=50,
    y=50,
)
text3.grid(
    row=2,
    column=1,
    padx=5,
    pady=5,
)
text3.configure(
    foreground="#222222",
    highlightcolor="#f7df1e",
    highlightbackground="#222222",
    highlightthickness=2.5,
    bg="white",
    state="readonly",
    width=30,
)

btnEvent = Button(root)
btnEvent.configure(
    bg="#f7df1e",
    fg="#222222",
    text="Calcular",
    font=("Arial", 14),
    command=multiplicacion,
)
btnEvent.grid(
    row=3,
    column=0,
    padx=10,
    pady=10,
)

btnEvent2 = Button(root)
btnEvent2.configure(
    bg="#f7df1e",
    fg="#222222",
    text="Limpiar",
    font=("Arial", 14),
    command=clear,
)
btnEvent2.grid(
    row=3,
    column=1,
    padx=10,
    pady=10,
)

btnEvent3 = Button(root)
btnEvent3.configure(
    bg="#f7df1e",
    fg="#222222",
    text="Cerrar",
    font=("Arial", 14),
    command=close,
)
btnEvent3.grid(
    row=3,
    column=2,
    padx=10,
    pady=10,
)
root.mainloop()
