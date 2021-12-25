import turtle
import pandas

screen = turtle.Screen()
guessed = 0
screen.title("Indian States and UTs Game")
screen.setup(1000, 1000)
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states and union teritories.csv")
guessed_state = []
states_list = data["States and Union Territories"].to_list()
state_font = ('Arial', 15, 'bold')

while guessed < 36:
    user_input = screen.textinput(title=f"{guessed}/36 States and UTs", prompt="Another state or UT?").title()
    if user_input in states_list:
        user_guess = data[data["States and Union Territories"] == user_input]
        print(user_guess.x, user_guess.y)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(user_guess.x), int(user_guess.y))
        t.write(user_input, font=state_font)
        guessed += 1
        guessed_state.append(user_input)
        states_list.remove(user_input)
    elif user_input == "Exit":
        print(states_list)
        data_to_learn = pandas.DataFrame(states_list)
        data_to_learn.to_csv("states_and_uts_to_learn.csv")
        break

#Ony needed when correcting or generating the coordinates for a new map/image
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()