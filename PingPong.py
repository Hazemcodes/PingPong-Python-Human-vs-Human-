import turtle
from tkinter import *
import winsound
import tkinter.font as font


def mainmenu():
    global wind1
    wind1 = Tk()
    wind1.title("PingPong")
    wind1.geometry("400x550+400+100")
    wind1.iconbitmap('icon/pingpong.ico')
    myFont = font.Font(size=20)

    startgame = Button(wind1, text="Start Game", bg="black", width=20, fg="Gold", bd=0,font=50 ,activeforeground="black", activebackground="black", command = start)
    startgame.place(x=30, y=120)

    quit = Button(wind1, text="Quit", bg="black", width=20, fg="Gold", bd=0, font=20, activeforeground="black",activebackground="black", command = wind1.quit)
    quit.place(x=30, y=220)

    startgame['font'] = myFont
    quit['font'] = myFont

    wind1['bg'] = "black"
    wind1.mainloop()

def start() :
    wind1.destroy()
    wn = turtle.Screen()
    wn.title("PingPong")
    wn.bgcolor("#0cf317")
    wn.setup(width=800,height=600)
    wn.tracer(0)

    # ***** Score *****
    score_a = 0
    score_b = 0

    # ***** Paddle A *****
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("red")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350,0)

    # ***** Paddle B *****
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("red")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350,0)

    # ***** Ball *****
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx = 0.5
    ball.dy = 0.5

    # ***** Pen *****
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Player A : 0 || Player B : 0",align="center",font=("Courier" , 24 , "bold"))
    try :

        # ***** Functions *****
        def paddle_a_up():
            y = paddle_a.ycor()
            y += 50
            paddle_a.sety(y)

        def paddle_a_down():
            y = paddle_a.ycor()
            y -= 50
            paddle_a.sety(y)

        def paddle_b_up():
            y = paddle_b.ycor()
            y += 50
            paddle_b.sety(y)

        def paddle_b_down():
            y = paddle_b.ycor()
            y -= 50
            paddle_b.sety(y)

        # ***** KeyBoard Binding *****
        wn.listen()
        wn.onkeypress(paddle_a_up,"w")
        wn.onkeypress(paddle_a_down,"s")
        wn.onkeypress(paddle_b_up,"Up")
        wn.onkeypress(paddle_b_down,"Down")

        # ***** Main game loop *****
        while True:
            wn.update()

            # ***** Move The Ball *****
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # ***** Border checking *****
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
                winsound.PlaySound("song\\Windows Default",winsound.SND_ASYNC)

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1
                winsound.PlaySound("song\\Windows Default",winsound.SND_ASYNC)

            if ball.xcor() > 390:
                ball.goto(0,0)
                ball.dx *= -1
                score_a += 1
                winsound.PlaySound("song\\chimes.wav",winsound.SND_ASYNC)
                pen.clear()
                pen.write("Player A : {} || Player B : {}".format(score_a,score_b),align="center",font=("Courier" , 24 , "bold"))

            if ball.xcor() < -390:
                ball.goto(0,0)
                ball.dx *= -1
                score_b += 1
                winsound.PlaySound("song\\chimes.wav",winsound.SND_ASYNC)
                pen.clear()
                pen.write("Player A : {} || Player B : {}".format(score_a,score_b),align="center",font=("Courier" , 24 , "bold"))

            # ***** Paddle and ball collisions
            if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
                ball.setx(340)
                ball.dx *= -1
                winsound.PlaySound("song\\Windows Default",winsound.SND_ASYNC)


            if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
                ball.setx(-340)
                ball.dx *= -1
                winsound.PlaySound("song\\Windows Default.wav",winsound.SND_ASYNC)
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    mainmenu()
