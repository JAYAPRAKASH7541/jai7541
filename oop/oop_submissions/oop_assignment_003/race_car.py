import math
from car import Car
class RaceCar(Car):
	sound="Peep Peep\nBeep Beep"
	def __init__(self,color,max_speed,acceleration,tyre_friction):
		super().__init__(color,max_speed,acceleration,tyre_friction)
		self.nitro=0
	def apply_brakes(self):
		if self._current_speed>=self._max_speed//2:
				self.nitro+=10
		super().apply_brakes()
	def accelerate(self):
		if self.nitro!=0 :
			self._current_speed+=math.ceil((self._acceleration*30)/100)
			self.nitro-=10
		super().accelerate()
	
			