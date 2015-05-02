
class one():
	
	def __init__(self, x):
		self.x = x



	def add2(self):
		return self.x + 2 

class two(one):

	def __init__(self, x, y):
		super(two, self).__init__(x)
		self.y = y
		



i1 = one(3)
i2 = one(4)
i3 = two(2, 2)

print i1.add2()
print i2.add2()
print i3.add2()
