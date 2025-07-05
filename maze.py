import turtle
screen = turtle.Screen()
screen.bgcolor("red")
screen.setup(width= 500, height= 500 )
obstacles = []

maze = ["XXXXXXXXXXXXXXX",
    "X             X",
    "X XXXXX XXXXX X",
    "X X     X     X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X XXX",
    "X     X X X   X",
    "XXXXX X X X XXX",
    "X     X   X   X",
    "XXXXXXX XXXXX X",
    "X             X",
    "XXXXXXXXXXXXX F"]

def create_maze():
    global finish
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            character = maze[y][x]
            screen_x = -280 + (x*25)
            screen_y = 280 - (y*25) 
          
            if character == "X":
                obstacle = turtle.Turtle()
                obstacle.speed(0)
                obstacle.shape("square")
                obstacle.color("black")
                obstacle.penup()
                obstacle.goto(screen_x,screen_y)
                obstacles.append(obstacle)
            elif character == "F":
                finish = turtle.Turtle()
                finish.shape("arrow")
                finish.color("purple")
                finish.penup()
                finish.goto(screen_x,screen_y)


player = turtle.Turtle()
player.shape("turtle")
player.color("black")
player.penup()
player.speed(5)

def move_up():
    x_new = player.xcor()
    y_new = player.ycor()+20
    if vaild_move(x_new,y_new):
        player.goto(x_new,y_new)
        win()

def move_down():
    x_new = player.xcor()
    y_new = player.ycor()-20
    if vaild_move(x_new,y_new):
        player.goto(x_new,y_new)
        win()

def move_right():
    x_new = player.xcor()+20
    y_new = player.ycor()
    if vaild_move(x_new,y_new):
        player.goto(x_new,y_new)
        win()


def move_left():
    x_new = player.xcor()-20
    y_new = player.ycor()
    if vaild_move(x_new,y_new):
        player.goto(x_new,y_new)
        win()

def vaild_move(x,y):
    for obstacle in obstacles:
        if obstacle.xcor() == x and obstacle.ycor() == y:
            return False 

    return True 

def win():
    if player.distance(finish)<2:
        finish.hideturtle()
        player.hideturtle()
        screen.kill()
        print("you have won")
       

screen.listen()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")



create_maze()
player.goto(0,0)
screen.mainloop()
