import turtle 
import random
import time 

turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor("black")
turtle.speed(0)

def draw_a_circle():
    turtle.penup()
    turtle.goto(random.randint(-200,200),random.randint(-200,200))
    turtle.color(
        random.randint(0,255),random.randint(0,255),random.randint(0,255)
    ) 

    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(random.randint(20,100))
    turtle.penup()
    turtle.end_fill()

delay = 0.2
start_time = time.time()
for i in range(60):
    draw_a_circle()
    time.sleep(delay)
    turtle.clear()
    delay = max(0.02,delay-0.02)

end_time = time.time()
elapsed_time = round(end_time-start_time,2)
turtle.penup()
turtle.goto(0,0)
turtle.color("white")
turtle.pendown()
turtle.write("animation time is {}".format(elapsed_time))
turtle.hideturtle()
turtle.done()