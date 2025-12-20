from turtle import *
from random import randint
import random

screen = getscreen()
screen.title("Гра 'Збери яблука'")
screen.bgcolor("black")

game = True

pole = Turtle()
pole.speed(0)
pole.color("whitesmoke")
pole.pu()
pole.goto(-150, 150)
pole.pd()
pole.begin_fill()
for i in range(4):
    pole.fd(325)
    pole.rt(90)
pole.end_fill()
pole.hideturtle()

skip = Turtle()
skip.pu()
skip.skip = 0
skip.color("red")
skip.goto(-140, 180)
skip.hideturtle()

colected = Turtle()
colected.pu()
colected.colected = 0
colected.color("green")
colected.goto(100, 180)
colected.hideturtle()
def nigga_secret():
    random_nigga = random.randint(1,5)
    if random_nigga == 3:
        print("NIGGERS")
def update_scores():
    skip.clear()
    skip.write(f"Пропущено: {skip.skip}", font=("Arial", 15, "bold"))
    colected.clear()
    colected.write(f"Зібрано: {colected.colected}", font=("Arial", 15, "bold"))

def game_over(result, color):
    global game
    game = False
    win_lose.color(color)
    win_lose.write(result, font=("Arial", 40, "bold"))

def skip_count():
    global game
    if not game: return
    skip.skip += 1
    update_scores()
    if skip.skip >= 3:
        game_over("GAME OVER", "red")

def colected_count():
    global game
    if not game: return
    colected.colected += 1
    update_scores()
    if colected.colected >= 10:
        game_over("YOU WON NIGGA", "green")
        colected.hidetutle()

update_scores()

basket = Turtle()
basket.color("brown")
basket.pu()
basket.sety(-120)
basket.shape("square")

def move_left():
    if game and basket.xcor() > -140:
        basket.setx(basket.xcor() - 20)
        nigga_secret()

def move_right():
    if game and basket.xcor() < 140:
        basket.setx(basket.xcor() + 20)
        nigga_secret()

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()


bomb = Turtle()
bomb.speed(0)
bomb.pu()
bomb.sety(120)
bomb.setx(randint(-140, 140))
bomb.color("black")
bomb.shape("circle")

ball = Turtle()
ball.speed(0)
ball.pu()
ball.sety(140)
ball.setx(randint(-140, 140))
ball.color("red")
ball.shape("circle")



win_lose = Turtle()
win_lose.hideturtle()
win_lose.pu()
win_lose.goto(-100, 0)

def ball_move():
    if not game: return

    ball.sety(ball.ycor() - 5)

    if ball.ycor() < -120:
        skip_count()
        ball.sety(140)
        ball.setx(randint(-140, 140)) 

    if ball.distance(basket) < 25 and ball.ycor() < -100:
        colected_count()
        ball.sety(140)
        ball.setx(randint(-140, 140)) 

        
        
ball_move() 
#============================================================
def bomb_move():
    if not game: return

    bomb.sety(ball.ycor() - 5)

    if bomb.ycor() < -120:
        colected_count()
        bomb.sety(140)
        bomb.setx(randint(-120, 140)) 

    if bomb.distance(basket) < 25 and ball.ycor() < -100:
        skip_count()
        bomb.sety(140)
        bomb.setx(randint(-120, 140))

        
    screen.ontimer(ball_move, 30)


    
 

 
bomb_move()

exitonclick()
#while True:                #yabluki.py copyright
#    print("NIGGERS")       #yabluki.py copyright