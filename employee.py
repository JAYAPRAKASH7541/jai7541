class Employee:
	emplos=0
	def __init__(self,f_name,l_name,pay):
		self.first=f_name
		self.last=l_name
		self.pay=pay
		self.email=f_name+'.'+l_name+'@comp.com'
		Employee.emplos+=1
	    
	def full_name(self):         
		return '{}{}'.format(self.first,self.last)
		


# print(Employee.emplos)
emp1=Employee("jai","prakawerwsh",90000)
emp2=Employee("jaip","prakash",90000)

print(emp1.last)
#print(Employee.emplos)
