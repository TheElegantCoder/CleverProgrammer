
import turtle

my_turtle = turtle.Turtle()
length = 90
angle = 90
my_turtle.speed(0)

def square(length, angle):

  my_turtle.forward(length)
  my_turtle.right(angle)
  my_turtle.forward(length)
  my_turtle.right(angle)
  my_turtle.forward(length)
  my_turtle.right(angle)
  my_turtle.forward(length)
  my_turtle.right(angle)


for x in range(100):
  square(length,angle)
  my_turtle.right(11)
# deleted the line print(x) - it works perfectly 