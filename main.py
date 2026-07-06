# ###########################################################
# GUI

# import tkinter as tk
from tkinter import  *
import json

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack() # asides .pack(), .place(0,0) - coordinate, or .grid(column=0, row= 2) - grid system can also be used to add components to the window

#Buttons
def action():
    print("Do something")
    website = website_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email
        }
    }

    # open file to read json data and update it
    with open("test.json", "r") as json_file_read:
        contents = json.load(json_file_read)
        contents.update(new_data)

    # open file to write the updated data
    with open("test.json", "w") as json_file_write:
        json.dump(contents, json_file_write, indent=4)

    website_entry.delete(0, END)
    email_entry.delete(0, END)

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
website_entry = Entry(width=30)
#Add some text to begin with
website_entry.insert(END, string="Amazon")
#Gets text in entry
print(website_entry.get())
website_entry.pack()

email_entry = Entry(width=30)
#Add some text to begin with
email_entry.insert(END, string="example@amazon.com")
email_entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

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