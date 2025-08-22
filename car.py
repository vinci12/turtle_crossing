from turtle import Turtle
import random
COLORS = ["red","blue","yellow","green","black"]

class Car(Turtle):
    def __init__(self):
        self.segments = []

    def create_car(self):
        random_choice=random.randint(1,6)
        if random_choice ==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            rand_y = random.randint(-250,250)
            new_car.goto(300,rand_y)
            self.segments.append(new_car)

    def move_car(self):
        for car in self.segments:
            car.backward(5)

