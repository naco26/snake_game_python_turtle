from turtle import Turtle
Wall_Size=290
POS=(0,270)
Poss=(-100,0)
FONT =("Arial,sans-serif",20)
GAME_OVER="Ꮆ卂爪乇 ㄖᐯ乇尺!"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_card=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(POS)
        self.write_score()
    
    def check_for_wall_collision(self,s,is_game_on):
        if s.xcor()>Wall_Size or s.xcor()<-Wall_Size or s.ycor()>Wall_Size or s.ycor()<-Wall_Size:
            is_game_on=False
            self.game_over()
        return is_game_on
    

    def game_over(self):
        self.goto(Poss)
        self.write(GAME_OVER,font=FONT)  

    def update_score(self):
        self.score_card+=1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score_card}",align="center",font=FONT)