import turtle as t
from Scoreboard import Score

positions=[(0,0),(-20,0),(-40,0)]
move_steps=20
Up = 90
Down = 270
Left = 180
Right = 0


class Snake:
    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]
        self.speed=1
    
    def create_snake(self):
        for pos in positions:
            self.add_snake(pos)
    
    def move(self):
        is_game_on=True
        for s in range(len(self.snake_body)-1,0,-1):
            self.snake_body[s].goto((self.snake_body[s-1].xcor(),
                                     self.snake_body[s-1].ycor()))
            
        self.head.forward(move_steps)
        
    
    def move_up(self):
        if self.head.heading()!=Down:
            self.head.setheading(Up)
            self.move()

    def move_down(self):
        if self.head.heading()!=Up:
            self.head.setheading(Down)
            self.move()

    def move_left(self):
        if self.head.heading()!=Right:
            self.head.setheading(Left)
            self.move()
    
    def move_right(self):
        if self.head.heading()!=Left:
            self.head.setheading(Right)
            self.move()
    def add_snake(self,new_pos):
        snake = t.Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(new_pos)
        self.snake_body.append(snake)
    
    def extend(self):
        self.add_snake(self.snake_body[-1].position())
        self.speed=self.speed+1
        for s in self.snake_body:
            s.speed(self.speed)

