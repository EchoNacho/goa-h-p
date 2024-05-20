from turtle import *


speed(20)
width(5)

#we want to paint a castle with king and queen

#step1 draw a squear

color("gray")
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
begin_fill()


forward(200)
left(90)
forward(200)
left(90)
forward(200)

end_fill()
begin_fill()

right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(400)
end_fill()
begin_fill()

forward(200)
right(90)
forward(200)
right(90)
forward(200)

end_fill()
#end of castle drawing roof

begin_fill()

penup()
goto(200,200)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)

forward(20)
left(180)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)

forward(20)
left(180)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)

forward(20)
left(180)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)

end_fill()

#drawing king


goto(0,200)


begin_fill()
right(90)
forward(2)
color("blue")
forward(50)
right(30)
forward(15)
right(150)
forward(60)
end_fill()

#drawing queen
penup()
goto(20,200)
left(180)
pendown()
color("pink")
forward(50)
right(30)
forward(10)
right(150)
forward(60)


penup()
goto(200,230)
pendown()
left(180)
color("gray")
forward(3)
color("orange")
forward(70)
right(90)
color("green")
begin_fill()
forward(60)
right(90)
forward(30)
right(90)
forward(60)
end_fill()


# Step 7: Write "GOA" on the flag
penup()
goto(215, 280)
pendown()
color("black")
write("GOA", font=("Arial", 16, "bold"))



penup()
goto(100,-200)
forward(50)
right(90)
pendown()
color("#8B4513")
begin_fill()
forward(150)
right(90)
forward(100)
right(90)
forward(150)
end_fill()

left(180)
forward(30)
color("black")
left(90)
forward(100)
left(180)
forward(10)
left(90)
forward(100)

# Draw lines on the door
penup()
goto(138, -170)  # Position the turtle for drawing lines
pendown()
for _ in range(3):
    forward(100)
    penup()
    backward(100)
    left(90)
    forward(30)
    right(90)
    pendown()






exitonclick()