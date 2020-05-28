import math
class ComplexNumber:
	def __init__(self,real_part=0,imaginary_part=0):
		
		
		if type(real_part)==str and type(imaginary_part)==str:
			raise ValueError("Invalid value for real and imaginary part")
		else:
			self.real_part=real_part
		
		if type(real_part)==str:
			raise ValueError("Invalid value for real part")
		else:
			self.real_part=real_part
		if type(imaginary_part)==str:
			raise ValueError("Invalid value for imaginary part")
		else:
			self.imaginary_part=imaginary_part
		
		
		
	
	def __add__(self, other):
		return ComplexNumber(self.real_part + other.real_part,self.imaginary_part + other.imaginary_part)
	
	def __sub__(self, other):
		return ComplexNumber(self.real_part - other.real_part,self.imaginary_part - other.imaginary_part)
		
	def __mul__(self, other):
		return ComplexNumber(self.real_part*other.real_part - self.imaginary_part*other.imaginary_part,self.imaginary_part*other.real_part + self.real_part*other.imaginary_part)
	def __abs__(self):
		abs_values= math.sqrt(self.real_part**2 + self.imaginary_part**2)
		return round(abs_values,3)
	def conjugate(self):
		return ComplexNumber(self.real_part,-(self.imaginary_part))
	
	def __eq__(self,other):
		  return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part
		  
	def __truediv__(self, other):
		sr, si, oor, oi = self.real_part, self.imaginary_part,other.real_part, other.imaginary_part # short forms
		r = float(oor**2 + oi**2)
		return ComplexNumber((sr*oor+si*oi)/r, (si*oor-sr*oi)/r)
	
	def __str__(self):
		if self.imaginary_part>=0:
			return "{}+{}i".format(self.real_part,self.imaginary_part)
		else:
			return"{}-{}i".format(self.real_part,-(self.imaginary_part))
	
		
	'''   def __div__(self, other):
        sr, si, or, oi = self.real, self.imag, \ 
                         other.real, other.imag # short forms
        r = float(or**2 + oi**2)
        return Complex((sr*or+si*oi)/r, (si*or-sr*oi)/r)'''