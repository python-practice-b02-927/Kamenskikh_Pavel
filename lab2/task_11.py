import turtle as t


t.shape('turtle')
t.left(90)
N=50
K=5
step=3
def infinit(step):
	for i in range(N):
		t.forward(step)
		t.left(360/N)
	for i in range(N):
		t.forward(step)
		t.right(360/N)
for i in range(K):
	infinit(step)
	step+=1
