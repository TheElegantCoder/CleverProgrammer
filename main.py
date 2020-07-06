# function with arguments, multiple arguments and loops 
# for x in range(10) that's a loop
# print (x)

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


for x in range(180):
  square(length,angle)
  my_turtle.right(2)
  print(x)

#Yey!!!! It worked! I created a loop!!!!

# Qazi's Code for Circle of Squares:

import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)
def square(length,angle)
  for i in range(100)
  square(100,90)
  my_turtle.right(11)

#Circle has 360 degrees
#360/10 -->36 We take the next undividible integer (11), so the squares are not overlapping.