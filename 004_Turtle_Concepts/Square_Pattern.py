import math
import turtle
import time

n = 480
m = 480/2 
div = 12
d = m//div
wn = turtle.Screen()
wn.title("Square Pattern")
wn.setup(width=603, height=603)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-m,m)
t.pendown()
for _ in range(4):
   t.fd(n)
   t.rt(90)


t1 = turtle.Turtle() # Q1
t1.speed(0)
t1.penup()
t1.goto(m,m)
t1.rt(90)

t2 = turtle.Turtle() # Q2
t2.speed(0)
t2.penup()
t2.goto(-m,m)

t3 = turtle.Turtle() # Q3
t3.speed(0)
t3.penup()
t3.goto(-m,-m)
t3.lt(90)

t4 = turtle.Turtle() # Q4
t4.speed(0)
t4.penup()
t4.goto(m,-m)
t4.rt(180)


for i in range(2*div):
   t.fd(d)
   t1.fd(d)
   t2.fd(d)
   t3.fd(d)
   t4.fd(d)
   t.goto(t1.position())
   t.goto(t4.position())
   t.goto(t3.position())
   t.goto(t2.position())


while True:
   wn.update()


