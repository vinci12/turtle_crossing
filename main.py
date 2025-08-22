from turtle import Screen
from player import Player
from car import Car
from score import Score
import time
score = Score()
player = Player()
car = Car()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up,"w")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()


    for c in car.segments:
        if c.distance(player) < 20:
            game_on=False
            score.game_over()

        if player.reached_finish():
            score.increase_score()
            player.reset()











screen.exitonclick()
