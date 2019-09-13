import turtle as t


t.shape('turtle')
N=50
K=3
def infinit():
	for i in range(N):
		t.forward(2)
		t.left(360/N)
	for i in range(N):
		t.forward(2)
		t.right(360/N)
for i in range(K):
	infinit()
	t.left(180/K)


