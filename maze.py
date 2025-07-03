import turtle
screen = turtle.Screen()
screen.bgcolor("red")
screen.setup(width= 500, height= 500 )
turtle.color("black")
turtle.shape("square")
reward = turtle.Turtle()
reward.color("blue")
reward.shape("triangle")
reward.penup()
reward.speed(0)
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

create_maze()
screen.mainloop()
