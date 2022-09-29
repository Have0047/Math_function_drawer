import turtle


turtle.Screen()
turtle.title("math function drawer")
turtle.bgcolor("white")
turtle.setup(width=500, height=500)
turtle.tracer(0)
turtle.penup()
turtle.bgpic("c.png")
turtle.forward(1000)

def coors():
    dot = turtle.Turtle()
    dot.shape("circle")
    dot.color("black")
    dot.goto(0, 0)
    dot.shapesize(stretch_wid=1, stretch_len=1)
    dot.goto(x=0,y=0)
    dot.pendown()
    dot.pensize(3)

def second_coors():
    dot = turtle.Turtle()
    dot.shape("circle")
    dot.color("black")
    dot.shapesize(stretch_wid=1, stretch_len=1)
    x = turtle.numinput("","Enter x coordinate", )*10
    y = turtle.numinput("","Enter y coordinate", )*10
    dot.goto(x=x, y=y)
    dot.pendown()
    dot.pensize(3)

while True:
    turtle.update()
    turtle.listen()
    turtle.onkeypress(coors, "p")# for restart the axises quistions
    turtle.onkeypress(second_coors, "r")# for restart the axises quistions
