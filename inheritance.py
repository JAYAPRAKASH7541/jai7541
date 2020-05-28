class Parent:
	x=1
	def __init__(self):
		self.y=2
	def Hello(self):
		print("Hi Madhu")
class Child(Parent):
	z=3
	
	def Hello(self):
		print("Hello from Child")
		super().Hello()

p,c=Parent(),Child()
print(p.x,p.y)
p.Hello()
print(c.x,c.y,c.z)
c.Hello()
print(Parent.x,Child.x)
print(isinstance(c,Child))
