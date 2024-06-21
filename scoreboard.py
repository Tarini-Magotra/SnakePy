from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
          self.high_score=int (data.read())
        self.score = 0
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 225)
        self.score_update()

    def score_update(self):
      self.clear()
      self.write(f"S: {self.score} HS: {self.high_score}",font=("Arial", 12, "normal"))
      self.score+=1
      

    def reset(self):
      if self.score-1>=self.high_score:
         self.high_score=self.score-1
         with open("data.txt",mode="w") as data:
           data.write(f"{self.high_score}")
      self.score=0
      self.score_update()

    '''def game_over(self):
      self.clear()
      self.color("black")
      self.goto(0,0)
      self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))'''
      
