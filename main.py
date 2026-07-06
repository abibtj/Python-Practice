

# ###########################################################
# GUI

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("test.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:  # runs only if there's a FileNotFoundError (Exception)
            with open("test.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else: # runs only if there was no exception
            #Updating old data with new data
            data.update(new_data)

            with open("test.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally: # always runs, regardless of exception or not
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("test.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Resources/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abc@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop() # keep window open until closed


# # ###########################################################
# # Data Analysis
#
# # CSV File Processing
#
# # import  csv
# import pandas
# from numpy.ma.extras import average
#
# # with open("./Resources/weather.csv", mode="r") as data_file:
#     # data = data_file.readlines() # direct line-by-line read
#     # data = csv.reader(data_file) # inbuilt csv package
#
# data = pandas.read_csv("./Resources/weather.csv") # returns a dataframe (table)
# temperatures = data["temp"] # returns a series (column)
# conditions = data.condition # returns a series (column)
# # print(f"average: {average(temperatures)}")
# # print(f"mean: {temperatures.mean()}")
# # print(f"max: {temperatures.max()}")
# # print(f"min: {temperatures.min()}")
# max_temp_row = data[data.temp == temperatures.max()]
# # print(max_temp_row)
#
# # create a dataframe from dictionary
# dic = {
#     "name" : ["Abeeb", "Ray", "Alm"],
#     "age" : [20, 10, 6]
# }
#
# # data_frame = pandas.DataFrame(dic)
# # data_frame.to_csv("test.csv") # writes data frame to .csv file
#
# squirrel_data = pandas.read_csv("./Resources/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
# black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
#
# s_dict = {
#     "color" : ["Gray", "Cinnamon", "Black"],
#     "count" : [gray_count, cinnamon_count, black_count]
# }
#
# data_frame = pandas.DataFrame(s_dict)
# data_frame.to_csv("test.csv") # writes data frame to .csv file
#
# with open("file1.txt") as f1:
#     with open("file2.txt") as f2:
#         a = f1.readlines()
#         b = f2.readlines()
#         c = [int(n) for n in a if n not in b]



# GAMES

# # ###########################################################
# # TURTLE CROSSING GAME
#
# from turtle import Screen
# from turtle_crossing import CarManager, Player, ScoreBoard
# import time
# import math
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
#
# screen = Screen()
# screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# screen.bgcolor("white")
# screen.title("Turtle Crossing")
# screen.tracer(0) # disable animation, requires manual screen update to see changes
#
# car_manager = CarManager()
# player = Player()
# score_board = ScoreBoard()
#
# screen.onkey(player.move, "Up")
#
# screen.listen()
#
# game_over = False
#
# while not game_over:
#     screen.update()
#     time.sleep(car_manager.car_speed)
#     car_manager.move_cars()
#
#     # Detect collision with a car
#     for car in car_manager.cars:
#         # if (car.distance(player) < 20) and (math.fabs(car.ycor() - player.ycor()) < 5):
#         if (car.distance(player) < 20):
#             score_board.game_over()
#             game_over = True
#
#     # Detect getting to destination
#     if (player.ycor() >= 280):
#         score_board.update()
#         player.goto(0,-280)
#         car_manager.car_speed *= 0.95 # Increase cars speed
#
# screen.exitonclick()


#
# # ###########################################################
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


#
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
#             # game_over = True
#             score_board.reset()
#             snake.reset()
#
# screen.exitonclick()

#
# #####################################################
# # TURTLES RACE GAME
#
# import random
# import  turtle as t
#
# screen = t.Screen()
# screen.setup(500,400)
# screen.title("Turtles Race")
# user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle colour will win the race?")
#
# t.colormode(255)
# tutles = []
# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
#
# for color in colors:
#     segment = t.Turtle(shape="turtle")
#     segment.color(color)
#     tutles.append(segment)
#
# y = [-90, -60, -30, 0, 30, 60, 90]
# for i in range(0, len(tutles)):
#     segment = tutles[i]
#     segment.penup()
#     segment.goto(x=-230, y=y[i])
#
# game_over = False
#
# while not game_over:
#     tut_index = -1
#     for segment in tutles:
#         tut_index += 1
#         segment.forward(random.randint(1,10))
#         pos_x = round(segment.xcor())
#         if pos_x >= 230:
#             game_over = True
#             if user_bet == colors[tut_index]:
#                 print("You won!")
#             else:
#                 print(f"You lost! The {colors[tut_index]} turtle won the race, but you bet on {user_bet} turtle")
#
# screen.exitonclick()