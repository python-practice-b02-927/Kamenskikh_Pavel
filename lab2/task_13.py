import turtle as t
t.shape('turtle')
N=100
def circle(step,'color'):
	color('color')
	begin_fill()
	for i in range(N):
		t.forward(step)
		t.left(360/N)
	end_fill()
circle(10,'Yellow')	
