import turtle
import numpy as np


def main(speed=0, bg_color="grey"):
    
    # create Turtle object
    turtle_screen = turtle.Screen()
    myTurtle = turtle.Turtle()
    
    # set speed to 'fastest = 0'
    myTurtle.speed(speed)
    # change background color
    turtle_screen.bgcolor(bg_color)
  
 
    colors = ["blue", "red", "yellow", "green", "cyan", "orange", "pink", "black", "purple", "grey"]


    for i in range(10):
        # define some params
        size = 25
        pos = [np.random.randint(-300, 300), np.random.randint(-300, 300)]
        cl=colors[i]
        """TODO: set snowflake color here (one of the colors defined above)"""
        myTurtle.color(cl)
        # Go to the start position of the snowflake
        myTurtle.penup()
        myTurtle.goto(pos[0], pos[1])
        myTurtle.pendown()

        # draw the snowflake
        for _ in range(10):
            snowflake_branch(size, myTurtle)
            myTurtle.left(45)
    turtle.exitonclick(10)

def snowflake_branch(size, myTurtle):
    # This function draws one branch of the snowflake.
    for _ in range(3):
        for _ in range(3):
            myTurtle.forward(size / 3)
            myTurtle.backward(size / 3)
            myTurtle.right(45)
        myTurtle.left(90)
        myTurtle.backward(size / 3)
        myTurtle.left(45)
    myTurtle.right(90)
    myTurtle.forward(size)


if __name__ == "__main__":
    main()
