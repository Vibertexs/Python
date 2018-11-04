
import random
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('pink')

caterpillar = Turtle('square', visible=False)
caterpillar.color('red')
caterpillar.speed('fastest')
caterpillar.penup()

leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
screen.register_shape('leaf', leaf_shape)

leaf = Turtle('leaf', visible=False)
leaf.color('green')
leaf.speed('fastest')
leaf.penup()

game_started = False
text_turtle = Turtle(visible=False)
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 150, 'bold'))

score_turtle = Turtle(visible=False)
score_turtle.speed('fastest')
score_turtle.penup()
x = (screen.window_width() / 2) - 50
y = (screen.window_height() / 2) - 50
score_turtle.setpos(x, y)
score_turtle.write(0, align='right', font=('Arial', 40, 'bold'))

def outside_window():
    left_wall = -screen.window_width() / 2
    right_wall = screen.window_width() / 2
    top_wall = screen.window_height() / 2
    bottom_wall = -screen.window_height() / 2

    x, y = caterpillar.pos()

    outside = \
        x < left_wall or \
        x > right_wall or \
        y < bottom_wall or \
        y > top_wall

    return outside

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    text_turtle.write('GAME OVER!', align='center', font=('Arial', 150, 'bold'))

def display_score(current_score):
    score_turtle.undo()  # erase previous score
    score_turtle.write(current_score, align=('right'), font=('Arial', 40, 'bold'))


# /\/\/\/\/\/\/\/\\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# /\/\\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
def place_leaf():
    leaf.hideturtle()
    leaf.setx(random.randint(-1250, 1250))
    leaf.sety(random.randint(-675, 675))
    leaf.showturtle()

def start_game():
    global game_started

    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 1
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)

        if caterpillar.distance(leaf) < 30:
            place_leaf()
            # caterpillar_length += 0
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 1
            score += 10
            display_score(score)

        if outside_window():
            game_over()
            break

def move_up():
    # if caterpillar.heading() == 0 or caterpillar.heading() == 180:
    caterpillar.setheading(90)

def move_down():
    # if caterpillar.heading() == 0 or caterpillar.heading() == 180:
    caterpillar.setheading(270)

def move_left():
    # if caterpillar.heading() == 90 or caterpillar.heading() == 270:
    caterpillar.setheading(180)

def move_right():
    # if caterpillar.heading() == 90 or caterpillar.heading() == 270:
    caterpillar.setheading(0)

screen.onkey(start_game, 'space')
screen.onkey(move_up, 'Up')
screen.onkey(move_right, 'Right')
screen.onkey(move_down, 'Down')
screen.onkey(move_left, 'Left')

screen.listen()
screen.mainloop()
