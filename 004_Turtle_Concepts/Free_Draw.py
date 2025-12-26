import turtle
import random
import time

#Screen set up
wn = turtle.Screen()
wn.title("Free Drawing")
wn.bgcolor('light blue')
wn.setup(width=603, height=603)
#wn.tracer(0) # turns of screen updates

# Our main draw head.
head = turtle.Turtle() #turtle object "head"
head.speed(0) # animation of movement speed 
head.shape('classic')
head.color('black')
# Turtle is designed to draw lines...to disable it we do penup
#head.penup()   # <-----comment this whoe line to play :-)
head.goto(0,0)
head.direction = 'stop'


# MOvement Functions
#Type 1
def move():
   if head.direction == 'up':
      y = head.ycor()
      head.sety(y+20)

   if head.direction == 'down':
      y = head.ycor()
      head.sety(y-20)

   if head.direction == 'left':
      x = head.xcor()
      head.setx(x-20)

   if head.direction == 'right':
      x = head.xcor()
      head.setx(x+20)

def go_up():
   if head.direction != 'down':
      head.direction = 'up'

def go_down():
   if head.direction != 'up':
      head.direction = 'down'

def go_left():
   if head.direction != 'right':
      head.direction = 'left'

def go_right():
   if head.direction != 'left':
      head.direction = 'right'



# Keyboard bindings :
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_left, 'Left')

# Main loop
# to turn on the screen updates we do :
while True:

   wn.update()
   move()
   time.sleep(0.05)
   if head.xcor() == 300 or head.xcor() == -300:
      head.penup()
      head.goto(0,0)
   if head.ycor() == 300 or head.ycor() == -300:
      head.penup()
      head.goto(0,0)
   
   #print(head.xcor, head.ycor)
   time.sleep(0.05)
   

wn.mainloop()