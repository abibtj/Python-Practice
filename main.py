
#
# ###########################################################
# # PONG GAME
#
# from turtle import Screen
# from pong import Paddle, Ball, ScoreBoard
# import time
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# TOP_EDGE = (SCREEN_HEIGHT // 2) - 5
# BOTTOM_EDGE = -1 * TOP_EDGE
# RIGHT_EDGE = (SCREEN_WIDTH // 2) - 80
# LEFT_EDGE = 40 - (SCREEN_WIDTH // 2)
# MAX_SCRORE = 3
#
# screen = Screen()
# screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# screen.bgcolor("black")
# screen.title("Pong Game")
# screen.tracer(0) # disable animation, requires manual screen update to see changes
#
# l_paddle = Paddle(-390)
# r_paddle = Paddle(383)
# ball = Ball(50)
# score_board = ScoreBoard()
#
# screen.onkey(l_paddle.move_up, "a")
# screen.onkey(l_paddle.move_down, "z")
#
# screen.onkey(r_paddle.move_up, "Up")
# screen.onkey(r_paddle.move_down, "Down")
#
# screen.listen()
#
# game_over = False
#
# while not game_over:
#     screen.update()
#     time.sleep(ball.move_speed)
#     ball.move()
#
#     # Detect collision with top and bottom edge of the screen
#     if ball.ycor() > (TOP_EDGE) or ball.ycor() < BOTTOM_EDGE:
#         ball.bounce_y()
#
#     # Detect collision with right paddle
#     elif r_paddle.distance(ball) < 30 and ball.xcor() > RIGHT_EDGE:
#         ball.bounce_x()
#
#     # Detect collision with left paddle
#     elif l_paddle.distance(ball) < 30 and ball.xcor() < LEFT_EDGE:
#         ball.bounce_x()
#
#     # Detect right paddle misses the ball
#     elif ball.xcor() > SCREEN_WIDTH // 2 + 5:
#         score_board.l_point()
#         ball.reset_position()
#
#     # Detect left paddle misses the ball
#     elif ball.xcor() < -1 * (SCREEN_WIDTH // 2 + 5):
#         score_board.r_point()
#         ball.reset_position()
#
#     if score_board.score_right == MAX_SCRORE or score_board.score_left== MAX_SCRORE:
#         score_board.game_over()
#         game_over = True
#
# screen.exitonclick()



# ##########################################################
# # SNAKE GAME
#
# from turtle import Screen
# from snake import Snake, Food, ScoreBoard
# import time
#
# SCREEN_SIZE = 600
# EDGE = SCREEN_SIZE // 2
#
# screen = Screen()
# screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
# screen.bgcolor("black")
# screen.title("Snake Game")
# screen.tracer(0) # disable animation, requires manual screen update to see changes
#
# snake = Snake()
# food = Food(SCREEN_SIZE)
# food.change_location()
# score_board = ScoreBoard()
#
# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
#
# game_over = False
#
# while not game_over:
#     screen.update()
#     time.sleep(snake.move_speed)
#     snake.move()
#
#     # Detect collision with food
#     if snake.head.distance(food) < 15:
#         score_board.update()
#         snake.grow()
#         food.change_location()
#
#     # Detect collision with wall
#     x_loc = snake.head.xcor()
#     y_loc = snake.head.ycor()
#
#     # Make collision with wall game over
#     # if x_loc >= (EDGE - 5) or x_loc <= (5 - EDGE) or y_loc >= (EDGE - 5) or y_loc <= (5 - EDGE):
#     #     game_over = True
#     #     score_board.game_over()
#
#     # Make collision with wall continue
#     if x_loc >= (EDGE - 5):
#         snake.head.goto((-1 * EDGE), y_loc)
#
#     if x_loc <= (5 - EDGE):
#         snake.head.goto(EDGE, y_loc)
#
#     if y_loc >= (EDGE - 5):
#         snake.head.goto(x_loc, (-1 * EDGE))
#
#     if y_loc <= (5 - EDGE):
#         snake.head.goto(x_loc, EDGE)
#
#     # Detect collision with tail
#     for segment in snake.segments[1:]:
#         if snake.head.distance(segment) < 10:
#             game_over = True
#             score_board.game_over()
#
# screen.exitonclick()


#####################################################
# TURTLES RACE

import random
import  turtle as t

screen = t.Screen()
screen.setup(500,400)
screen.title("Turtles Race")
user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle colour will win the race?")

t.colormode(255)
tutles = []
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for color in colors:
    segment = t.Turtle(shape="turtle")
    segment.color(color)
    tutles.append(segment)

y = [-90, -60, -30, 0, 30, 60, 90]
for i in range(0, len(tutles)):
    segment = tutles[i]
    segment.penup()
    segment.goto(x=-230, y=y[i])

game_over = False

while not game_over:
    tut_index = -1
    for segment in tutles:
        tut_index += 1
        segment.forward(random.randint(1,10))
        pos_x = round(segment.xcor())
        if pos_x >= 230:
            game_over = True
            if user_bet == colors[tut_index]:
                print("You won!")
            else:
                print(f"You lost! The {colors[tut_index]} turtle won the race, but you bet on {user_bet} turtle")

screen.exitonclick()