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
        self.create_snake()
        self.move_speed = 0.2
        self.head = self.segments[0]

    def create_snake(self):
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
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)
