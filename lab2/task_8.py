import turtle as t


t.shape('turtle')
K=100
step=5
for i in range(K):
	t.forward(step)
	t.left(90)
	step+=5
