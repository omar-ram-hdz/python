import turtle
import time
import random


posponer = 0.1

# ventana
wn = turtle.Screen()
wn.title("Juego-Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# cabeza
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"
cabeza.color("green")

# texto
texto = turtle.Turtle()
texto.speed(0)
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.color("white")
texto.write(
    "Score: 0      High_score: 0", align="center", font=("courier", 24, "normal")
)

score = 0
high_score = 0

# comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0, 150)
comida.color("red")


# funciones para el teclado
def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def derecha():
    cabeza.direction = "right"


def izquierda():
    cabeza.direction = "left"


# lista para los segmentos de la serpiente
segmentos = []


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)


# controles del juego
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(derecha, "Right")
wn.onkeypress(izquierda, "Left")
# --------------LOOP PRINCIPAL----------------------
while True:
    wn.update()

    # colisión con los bordes

    if (
        cabeza.xcor() > 280
        or cabeza.xcor() < -280
        or cabeza.ycor() > 280
        or cabeza.ycor() < -280
    ):
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        for segmento in segmentos:
            segmento.hideturtle()

        segmentos.clear()

        # borrando texto
        score = 0
        texto.clear()
        texto.write(
            "Score: {}      High_score: {}".format(score, high_score),
            align="center",
            font=("courier", 24, "normal"),
        )

    # colisión con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        # nuevo segmento
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.penup()
        nuevo_segmento.goto(0, 0)
        nuevo_segmento.direction = "stop"
        nuevo_segmento.color("cyan")
        segmentos.append(nuevo_segmento)

        score += 10

        if score > high_score:
            high_score = score
            if score >= 0:
                texto.color("white")
            if score >= 50:
                texto.color("red")
            if score >= 100:
                texto.color("yellow")

        texto.clear()
        texto.write(
            "Score: {}      High_score: {}".format(score, high_score),
            align="center",
            font=("courier", 24, "normal"),
        )

    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()

    # colision con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            # borrar segmentos
            for segmento in segmentos:
                segmento.hideturtle()
            segmentos.remove(nuevo_segmento)

            segmentos.clear()
            # borrando texto
            score = 0
            texto.clear()
            texto.write(
                "Score: {}      High_score: {}".format(score, high_score),
                align="center",
                font=("courier", 24, "normal"),
            )

    time.sleep(posponer)

# print("Hola: {} Adios{}".format(var1,var2))
# Format es para interpolar, se pone en secuencia, dentro de los {}
