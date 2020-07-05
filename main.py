# function with arguments, multiple arguments and loops 
# for x in range(10)
# print x

import turtle

my_turtle = turtle.Turtle()
length = 70
angle = 90
def square(length, angle):

  my_turtle.forward(length)
  my_turtle.right(angle)
  my_turtle.forward(length)
  my_turtle.right(angle)
  my_turtle.forward(length)
  my_turtle.right(angle)
  my_turtle.forward(length)
  my_turtle.right(angle)

square(length, angle)
my_turtle.right(45)
square(length, angle)
my_turtle.right(45)
square(length, angle)
my_turtle.right(45)
square(length, angle)
my_turtle.right(45)
square(length, angle)
my_turtle.right(45)
square(length, angle)
my_turtle.right(45)
square(length, angle)
my_turtle.right(45)
square(length, angle)
my_turtle.right(45)

