from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.timmys = []
        self.create_timmys()

    def create_timmys(self):
        for position in STARTING_POSITIONS:
            self.add_timmy(position)

    def add_timmy(self, position):
        timmy = Turtle(shape='square')
        timmy.color('white')
        timmy.penup()
        timmy.goto(position)
        self.timmys.append(timmy)

    def extend(self):
        self.add_timmy(self.timmys[-1].position())

    def move(self):
        for timmy_num in range(len(self.timmys) - 1, 0, -1):
            new_x = self.timmys[timmy_num - 1].xcor()
            new_y = self.timmys[timmy_num - 1].ycor()
            self.timmys[timmy_num].goto(new_x, new_y)
        self.timmys[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.timmys[0].heading() != DOWN:
            self.timmys[0].setheading(UP)

    def down(self):
        if self.timmys[0].heading() != UP:
            self.timmys[0].setheading(DOWN)

    def left(self):
        if self.timmys[0].heading() != RIGHT:
            self.timmys[0].setheading(LEFT)

    def right(self):
        if self.timmys[0].heading() != LEFT:
            self.timmys[0].setheading(RIGHT)

    def reset_timmys(self):
        for timmy in self.timmys:
            timmy.goto(500, 0)
        self.timmys.clear()
        self.create_timmys()
