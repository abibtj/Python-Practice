import random
from turtle import Turtle

# STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
COLORS = ["red","orange","yellow","green","blue","indigo","violet","pink"]



NUMBER_OF_CARS = 20
ALIGNMENT = "center"
SMALL_FONT = ("Arial",20, "normal")
INITIAL_SLEEP_TIME = 0.3

class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = INITIAL_SLEEP_TIME
        for _ in range(NUMBER_OF_CARS):
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.turtlesize(1, 2)
            car.goto(random.randint(-400, 400), random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.goto((car.xcor() - 10), car.ycor()) # move backward
            if car.xcor() < -400:
                car.goto(400, random.randint(-250, 250))
                car.color(random.choice(COLORS))

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(0,-280)
        self.setheading(90)

    def move(self):
        self.forward(20)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 260)
        # self.color("white")
        self.pencolor("black")
        self.hideturtle()
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=SMALL_FONT)

    def game_over(self):
        # self.write(f"GAME OVER!", False, align=ALIGNMENT, font=SMALL_FONT)
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=SMALL_FONT)

