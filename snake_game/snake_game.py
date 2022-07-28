import turtle
import time
import random

#creating game screen. x and y axis selected 700
gameScreen = turtle.Screen()
gameScreen.tracer(0)
gameScreen.setup(600,600)
gameScreen.bgcolor("black") #backgroundcolor choice


#creating of the snake. shape and color selected square and white
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.speed(0) #this is not the movement speed. this is the animation speed. this will keep snake on the screen all the time
snake.penup() #the trace left behind by the snake is being erased
snake.goto(-200,0) #the coordinate from which the snake will start
snake.direction = "stop"


#creating of the bait. shape and color selected square and red
bait = turtle.Turtle()
bait.shape("square")
bait.color("red")
bait.speed(0) #this is not the movement speed. this is the animation speed. this will keep snake on the screen all the time
bait.penup() #the trace left behind by the snake is being erased
bait.goto(0,0) #the coordinate from which the snake will start
bait.direction = "stop"


#function to change the direction of the snake
def up():
    if snake.direction != "down":
        snake.direction = "up"
def down():
    if snake.direction != "up":
        snake.direction = "down"
def right():
    if snake.direction != "left":
        snake.direction = "right"
def left():
    if snake.direction != "right":
        snake.direction = "left"


#assignment of direction functions to keyboard keys: wasd keys
gameScreen.listen()
gameScreen.onkeypress(up,"w")
gameScreen.onkeypress(down,"s")
gameScreen.onkeypress(right,"d")
gameScreen.onkeypress(left,"a")
#assignment of direction functions to keyboard keys: arrow keys
gameScreen.listen()
gameScreen.onkeypress(up,"Up")
gameScreen.onkeypress(down,"Down")
gameScreen.onkeypress(right,"Right")
gameScreen.onkeypress(left,"Left")


#function that allows it to move according to the changing snake direction
def move():
    if snake.direction == "up":
            y = snake.ycor()
            snake.sety(y+20)
    if snake.direction == "down":
            y = snake.ycor()
            snake.sety(y-20)
    if snake.direction == "right":
            x = snake.xcor()
            snake.setx(x+20)
    if snake.direction == "left":
            x = snake.xcor()
            snake.setx(x-20)



parts = [] #for the grow function

#game will always stay open with infinite loop
while True:
    gameScreen.update()


    #made the snake die if it touches the edges
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(-200,0)
        snake.direction = "stop"

        #when the game is over the snake length should return to its original state
        for i in parts:
            i.goto(2000,2000)

        parts.clear()


    # function that measures the distance between bait and snake
    if snake.distance(bait) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        bait.goto(x,y)

        # function that makes the snake grow if the snake eats bait
        newPart = turtle.Turtle()
        newPart.speed(0)
        newPart.shape("square")
        newPart.penup()
        newPart.color("white")
        parts.append(newPart)

    # parts are joined together. the last part quantity is added to the snake
    #It will count to 0. It will count down by 1 each. It will count up to (parts-1)
    # parts are joined together.
    for i in range(len(parts) - 1,0,-1):
        x = parts[i-1].xcor()
        y = parts[i-1].ycor()
        parts[i].goto(x,y)

    # the last part quantity is added to the snake
    if len(parts) > 0:
        x = snake.xcor()
        y = snake.ycor()
        parts[0].goto(x,y)


    move()

    # the function where the snake dies when it hits itself
    for i in parts:
        if i.distance(snake) < 20:
           time.sleep(1)
           snake.goto(-200,0)
           snake.direction = "stop"

           for i in parts:
               i.goto(2000,2000)

           parts.clear()

    time.sleep(0.1) #added 0.1 waiting time for the app to run


