import turtle as t


t.shape('turtle')
t.left(90)
N=30
K=5
def half_circle(step):
	for i in range(N):
		t.forward(step)
		t.right(180/N)
for i in range(K):
	half_circle(5)
	half_circle(1)
half_circle(5)	
