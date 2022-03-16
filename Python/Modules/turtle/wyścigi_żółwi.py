from ast import alias
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
# screen.bgpic('road.gif')

ALIGN = "right"
FONT = ("Courier", 20, "bold")

y_positions = [-260, -172, -85, 2, 82, 175, 260]
colors = ["white", "red", "orange", "yellow", "green", "blue", "purple"]
colors2 = {
    "white": "Biały",
    "red": "Czerwony",
    "orange": "Pomarańczowy",
    "yellow": "Źółty",
    "green": "Żielony",
    "blue": "Niebieski",
    "purple": "Fioletowy"
}

all_turtle = []
user_bet = screen.textinput('Daj swój zakład', prompt=f'Jaki żółw (kolor) \n{", ".join(colors2.values())}')

for index in range(0, 7):
    new_tur = Turtle(shape="turtle")
    new_tur.shapesize(2)
    new_tur.speed('fastest')
    new_tur.penup()  # podnosi żółwika żeby nie rysował
    new_tur.goto(x=-350, y=y_positions[index])
    new_tur.color(colors[index])
    all_turtle.append(new_tur)

is_on = True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 330:
            is_on = False
            winner = turtle.pencolor()  # purple
            winner = colors2[winner]
            if winner == user_bet:
                turtle.write(f'Wygrałeś!! {winner.capitalize()} żółw wygrał', font=FONT, align=ALIGN)
            else:
                turtle.write(f'Przegrałeś! Wygrał {winner.lower()} żółw', font=FONT, align=ALIGN)
        random_pace = random.randint(0, 7)
        turtle.forward(random_pace)

screen.exitonclick()
