from fileinput import close
from turtle import Turtle
import random

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Snake:

    def __init__(self):
        self.segments = []
        self.create_segments()
        self.move_speed = 0.2
        self.head = self.segments[0]

    def create_segments(self):
        for position in STARTING_POSITION:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for i in range((len(self.segments) - 1), 0, -1):
            prev_x = self.segments[i - 1].xcor()
            prev_y = self.segments[i - 1].ycor()
            self.segments[i].goto(prev_x, prev_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        self.segments.append(segment)
        self.move_speed *= 0.95

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_segments()
        self.head = self.segments[0]

class Food(Turtle):

    def __init__(self, scr_size):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.screen_size = scr_size
        self.change_location()

    def change_location(self):
        max_position = self.screen_size // 2 - 20
        x = random.randint(-1 * max_position, max_position)
        y = random.randint(-1 * max_position, max_position)
        self.goto(x, y)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.score = -1
        self.high_score = self.read_high_score()
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}, High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self ):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
        self.score = -1
        self.update()
        self.write_high_score(self.high_score)

    def write_high_score(self, high_score):
        with open("Resources/snake_game_high_score.txt", mode="w") as file: # file closes automatically after use
            file.write(high_score)

    def read_high_score(self):
        with open("Resources/snake_game_high_score.txt", mode="r") as file: # file closes automatically after use
            return file.read()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)
