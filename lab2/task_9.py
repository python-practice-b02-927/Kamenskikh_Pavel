import turtle as t
import math


from math import sin, pi
t.shape('turtle')
n=3
N=n+3
R=15
r=R

while n<=N:
	figure(n,R)
	t.penup()
	t.forward(r)
	t.pendown()
	n+=1
	R+=r


def figure(a,r):
	t.left(90+180/a)
	for i in range(a):
		t.forward(2*sin(pi/a)*r)
		t.left(360/a)
	t.right(90+180/a)
		
		 

