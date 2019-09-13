import turtle as t


t.shape('turtle')
number=12
step=50
for i in range(number):
	t.forward(step)
	t.stamp()
	t.right(180)
	t.forward(step)
	t.left(180-360/number)

	
