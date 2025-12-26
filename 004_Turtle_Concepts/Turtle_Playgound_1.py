import turtle
import time
import random
import math

# Screen setup

wn = turtle.Screen()
wn.title("Play Ground")
wn.bgcolor('light blue')
wn.setup(width=603, height=603)
#wn.tracer(0) # turns of screen updates

# Creating a turte:

t = turtle.Turtle()
t.speed(0)
t.color('dark blue')
t.shape('classic')
t.direction = 'stop'

def circle(r, co_ordintes, speed=0):
   '''Draws a circle of radius 'r' at co-ordinates given.'''
   t.penup()
   t.goto(co_ordintes)
   t.pendown()
   t.circle(r)

# Awesome Circle Pattern

for i in range(99):
   circle(69, (0,0))
   t.left(9)

# Awesome circular and elliptical pattterns 
'''
for i in range(360):
   x = 207*math.cos(i)     # Angles in radians
   y = 306*math.sin(i)
   t.speed(9)
   t.goto(x,y)'''
# drawing circle without built in function
'''
radius = 306
t.penup()
t.goto(radius,0)
t.pendown()
for i in range(361):
   x = radius*math.cos(math.radians(i))  # Angles in degrees
   y = radius*math.sin(math.radians(i))
   t.speed(9)
   t.goto(x,y)
'''  
'''
# Spiral box 1!
m = 4
angle = 72
width = 1
t.pendown()
for _ in range(399):
   t.forward(m)
   t.right(angle)
   t.forward(m)
   m+=width
'''
'''
# Spiral box 2!
m = 3*18
angle1 = 18
angle2 = 81
angle3 = 125   # <--- you can comment this
width = 0.15*2
t.pendown()
for i in range(299):
   t.forward(m)
   if i%2 == 0:
      t.right(angle1)
   else:
      t.right(angle2)
   t.forward(m)
   t.right(angle3)    # <--- you can comment this
   t.right(50)
   m+=width

'''


# while running only the abive command the sceen just stays for few ms... to prevent that we udate the window
# in an while loop

while True:

   wn.update()

#wn.mainloop()