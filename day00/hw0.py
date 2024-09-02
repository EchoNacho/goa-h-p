from turtle import *


speed(20)
width(5)

#we want to paint a hous

#step1 draw a squear

color("blue")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(200)

end_fill()
#end of square (drawing door)


left(90)
forward(70)

color("yellow")
begin_fill()
left(90)
forward(91)

left(90)
left(180)

forward(50)
left(180)
left(90)
forward(91)

end_fill()
#door drawing completed drawing roof
color("red")
begin_fill()

penup()
goto(200,200)
pendown()

left(220)
forward(160)
left(101)
forward(160)
left(129)
forward(206)

# Adding this part to close the roof fill properly
penup()
goto(200,200)
pendown()

end_fill()
#roof drawn drawing windows
color("purple")


penup()
goto(40,100)

pendown()
left(90)
left(90)
forward(22.5)
penup()
goto(40,100)
pendown()
left(180)
forward(22.5)
left(90)
forward(45)
left(90)
forward(45)
left(91)
forward(45)


#second window
color("purple")

penup()
goto(183,100)
right(91)

pendown()
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)

exitonclick()
