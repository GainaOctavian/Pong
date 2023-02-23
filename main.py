# Joc de pong


import turtle
import winsound

wn = turtle.Screen()  # wn = window
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scor
scor_a = 0
scor_b = 0

# Paleta A
paleta_a = turtle.Turtle()
paleta_a.speed(0)
paleta_a.shape("square")
paleta_a.color("white")
paleta_a.shapesize(stretch_wid=5, stretch_len=1)
paleta_a.penup()
paleta_a.goto(-350, 0)

# Paleta B
paleta_b = turtle.Turtle()
paleta_b.speed(0)
paleta_b.shape("square")
paleta_b.color("white")
paleta_b.shapesize(stretch_wid=5, stretch_len=1)
paleta_b.penup()
paleta_b.goto(350, 0)

# Minge
minge = turtle.Turtle()
minge.speed(0)
minge.shape("square")
minge.color("white")
minge.penup()
minge.goto(0, 0)
minge.dx = 0.35
minge.dy = 0.35

# pix
pix = turtle.Turtle()
pix.speed(0)
pix.color("white")
pix.penup()
pix.hideturtle()
pix.goto(0, 260)
pix.write("Jucator A: 0  Jucator B: 0", align="center", font=("Courier", 24, "normal"))

# Functii


def paleta_a_up():
    y = paleta_a.ycor()
    y += 20
    paleta_a.sety(y)


def paleta_a_down():
    y = paleta_a.ycor()
    y -= 20
    paleta_a.sety(y)


def paleta_b_up():
    y = paleta_b.ycor()
    y += 20
    paleta_b.sety(y)


def paleta_b_down():
    y = paleta_b.ycor()
    y -= 20
    paleta_b.sety(y)


# Keybindings
wn.listen()
wn.onkeypress(paleta_a_up, "w")
wn.onkeypress(paleta_a_down, "s")
wn.onkeypress(paleta_b_up, "Up")
wn.onkeypress(paleta_b_down, "Down")

# Bucla principala a jocului
while True:
    wn.update()

    minge.setx(minge.xcor() + minge.dx)
    minge.sety(minge.ycor() + minge.dy)

    # Verificarea marginilor
    if minge.ycor() > 290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        minge.sety(290)
        minge.dy *= -1
    if minge.xcor() > 390:
        minge.goto(0, 0)
        minge.dx *= -1
        scor_a += 1
        pix.clear()
        pix.write("Jucator A: {}  Jucator B: {}".format(scor_a, scor_b), align="center", font=("Courier", 24, "normal"))
    if minge.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        minge.sety(-290)
        minge.dy *= -1
    if minge.xcor() < -390:
        minge.goto(0, 0)
        minge.dx *= -1
        scor_b += 1
        pix.clear()
        pix.write("Jucator A: {}  Jucator B: {}".format(scor_a, scor_b), align="center", font=("Courier", 24, "normal"))

    # Coliziune ale paletei si a mingii
    if minge.xcor() > 340 and minge.xcor() < 350 and (minge.ycor() < paleta_b.ycor() +40 and minge.ycor() > paleta_b.ycor() -40):
        minge.setx(340)
        minge.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if minge.xcor() < -340 and minge.xcor() > -350 and (minge.ycor() < paleta_a.ycor() + 40 and minge.ycor() > paleta_a.ycor() -40):
        minge.setx(-340)
        minge.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
