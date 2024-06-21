from turtle import Turtle
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
  def __init__(self):
    self.segments=[]
    self.create_snake()
    self.head=self.segments[0]

  def create_snake(self):
    for position in STARTING_POSITION:
      self.add_segment(position)
      

  def move(self):
      
        for seg in range(len(self.segments) - 1, 0, -1):
            x_coord = self.segments[seg - 1].xcor()
            y_coord = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_coord, y_coord)
        self.head.forward(DISTANCE)

  def up(self):
    if self.head.heading()!=DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading()!=UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading()!=RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading()!=LEFT:
      self.head.setheading(RIGHT)

  def add_segment(self,position):
      snake = Turtle()
      snake.shape("square")
      snake.penup()
      snake.speed("fast")
      snake.color("black")
      snake.hideturtle()
      snake.goto(position)
      snake.color("white")
      snake.showturtle()
      self.segments.append(snake)

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def reset(self):
    for seg in self.segments:
      seg.color("black")
      seg.hideturtle()
      seg.goto(1000,1000)#basically we are sending our previous snake to a whole new
      #place which is outside our screen
    self.segments.clear()#clears everything in that list
    self.create_snake()#creates a new snake
    self.head=self.segments[0]#initialising our snake from 0th square
    #but without step 1 we will get an error as the previous snake wont disappear
    
    
    


    
    
      