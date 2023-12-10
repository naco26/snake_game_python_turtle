import turtle as t
from  snake import Snake
from Scoreboard import Score
from ball import Ball
import time

#screen setup
screen = t.Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game 2023")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
FONT =("Arial,sans-serif",20)


#snake body
my_snake=Snake()

#ball
my_ball=Ball()


#ScoreCard
score = Score()

is_game_on = True
screen.onkey(key="Up",fun=my_snake.move_up)
screen.onkey(key="Down",fun=my_snake.move_down)
screen.onkey(key="Left",fun=my_snake.move_left)
screen.onkey(key="Right",fun=my_snake.move_right)
while is_game_on:
    #moving snake
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    #Detect collision with ball
    if my_snake.head.distance(my_ball) < 17:
        my_ball.random_ball()
        my_snake.extend()
        score.update_score()

    #Detect collision with wall
    is_game_on=score.check_for_wall_collision(my_snake.head,is_game_on)

    #Detect collision with it's tail
    for s in my_snake.snake_body[1:]:
        if my_snake.head.distance(s)<10:
            is_game_on=False
            score.game_over()


    

screen.exitonclick()