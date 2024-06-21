from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=500, width=500)
screen.title("Snake Game")
screen.listen()

my_snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    
    if my_snake.head.distance(food) < 15:
        food.refresh()
        score.score_update()
        my_snake.extend()
      
    if my_snake.head.xcor()>230 or my_snake.head.ycor()>230:
        score.reset()
        my_snake.reset()
      
    if my_snake.head.xcor()<-230 or my_snake.head.ycor()<-230:
        score.reset()
        my_snake.reset()

    for segment in my_snake.segments:
      if segment==my_snake.head:
        pass
      elif my_snake.head.distance(segment)<10:
        score.reset()
        my_snake.reset()
       
        
      
        
      
screen.mainloop()
