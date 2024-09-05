from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("silly snake game")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.timmys[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score += 1
        score.score_refresh()

    if (snake.timmys[0].xcor() >= 300 or snake.timmys[0].xcor() <= -300 or snake.timmys[0].ycor() >= 300
            or snake.timmys[0].ycor() <= -300):
        score.reset()
        snake.reset_timmys()

    for timmy in snake.timmys[1:]:
        if snake.timmys[0].distance(timmy) < 10:
            score.reset()
            snake.reset_timmys()

screen.exitonclick()
