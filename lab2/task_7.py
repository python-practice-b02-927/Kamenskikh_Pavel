import turtle as t
t.shape('turtle')
step=1
Betta=0
N=50
K=20
for i in range(K):
	while Betta<=180:
		t.forward(step)
		t.left(360/N)
		Betta+=360/N
	step+=1
	Betta=0
	
	
	
