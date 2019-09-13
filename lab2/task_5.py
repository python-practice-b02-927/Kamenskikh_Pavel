import turtle as t


t.shape('turtle')
N=40
N1=N/2
while N<=20*N1:
	for i in range(4):
		t.forward(N)
		t.left(90)
	t.penup()
	N+=N1*2
	for i in range(2):
		t.right(90)
		t.forward(N1)
	t.right(180)
	t.pendown()

