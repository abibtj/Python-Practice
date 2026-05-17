from turtle import Turtle

ALIGNMENT = "center"
BIG_FONT = ("Arial", 60, "normal")
SMALL_FONT = ("Arial",20, "normal")

class Paddle(Turtle):

    def __init__(self, x_cord):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(4, 0.5)
        self.goto(x_cord, 0)
        # self.score = 0

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 50)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 50)

class Ball(Turtle):

    def __init__(self, direction):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(direction)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.15

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.forward(20)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.95

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,200)
        self.score_right = 0
        self.score_left = 0
        self.update()

    def r_point(self):
        self.score_right += 1
        self.update()

    def l_point(self):
        self.score_left += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score_left} : {self.score_right}", False, align=ALIGNMENT, font=BIG_FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=SMALL_FONT)

