class Pokemon:
	sound_by_animal=""
	def __init__(self,name,level):
		self._master=None
		if name=="":
			raise ValueError("name cannot be empty")
		else:
			self._name=name
		if level <=0:
			raise ValueError("level should be > 0")
		else:
			self._level=level
	@property
	def master(self):
		if self._master==None:
			print("No Master")
		else:
			return self._master
	@property
	def level(self):
		return self._level
	
	@property
	def name(self):
		return self._name
		
	def __str__(self):
		return ("{} - Level {}".format(self.name,self.level))
		
		
	@classmethod
	def make_sound(cls):
		print(cls.sound_by_animal)
	
class Running_animal:
	
	run_animal=""
	
	@classmethod
	def run(cls):
		print("{} running...".format(cls.run_animal))
		

class Swimming_animal:
	
	swim_animal=""
	
	@classmethod
	def swim(cls):
		print("{} swimming...".format(cls.swim_animal))
		
class Flying_animal:
	
	fly_animal=""
	
	@classmethod
	def fly(cls):
		print("{} flying...".format(cls.fly_animal))

class Pikachu(Pokemon,Running_animal):
	
	sound_by_animal="Pika Pika"
	run_animal="Pikachu"

	def attack(self):
		self.type_attack="Electric attack"
		print("{} with {} damage".format(self.type_attack,(self.level*10)))
		

class Squirtle(Pokemon,Running_animal,Swimming_animal):
	
	sound_by_animal="Squirtle...Squirtle"
	run_animal="Squirtle"
	swim_animal="Squirtle"
	
	def attack(self):
		self.type_attack="Water attack"
		print("{} with {} damage".format(self.type_attack,(self.level*9)))
	
class Pidgey(Pokemon,Flying_animal):
	
	sound_by_animal="Pidgey...Pidgey"
	fly_animal="Pidgey"
	
	def attack(self):
		self.type_attack="Air attack"
		print("{} with {} damage".format(self.type_attack,(self.level*5)))
	
class Swanna(Pokemon,Flying_animal,Swimming_animal):
	
	sound_by_animal="Swanna...Swanna"
	fly_animal="Swanna"
	swim_animal="Swanna"
	
	def attack(self):
		self.type_attack="Water attack"
		self.types_attack="Air attack"
		print("{} with {} damage".format(self.type_attack,(self.level*9)))
		print("{} with {} damage".format(self.types_attack,(self.level*5)))

class Zapdos(Pokemon,Flying_animal):
	
	sound_by_animal="Zap...Zap"
	fly_animal="Zapdos"
	
	def attack(self):
		self.type_attack="Electric attack"
		self.types_attack="Air attack"
		print("{} with {} damage".format(self.type_attack,(self.level*10)))
		print("{} with {} damage".format(self.types_attack,(self.level*5)))

class Island:
	
	total_islands=[]
	def __init__(self,name, max_no_of_pokemon, total_food_available_in_kgs):
		
		
		self._pokemon_left_to_catch=0
		self._name=name
		self._max_no_of_pokemon=max_no_of_pokemon
		self._total_food_available_in_kgs = total_food_available_in_kgs
		self.total_islands.append(self)
		
	@property
	def name(self):
		return self._name
	
	@property
	def pokemon_left_to_catch(self):
		return self._pokemon_left_to_catch
		
	@property
	def max_no_of_pokemon(self):
		return self._max_no_of_pokemon
	
	@property
	def total_food_available_in_kgs(self):
		return self._total_food_available_in_kgs
		
	def __str__(self):
		return ("{} - {} pokemon - {} food".format(self._name,
		self._pokemon_left_to_catch,self._total_food_available_in_kgs))
		
	def add_pokemon(self,pokemon):
		if self._pokemon_left_to_catch>=self._max_no_of_pokemon:
			print("Island at its max pokemon capacity")
		else:
			self._pokemon_left_to_catch+=1
	
	@classmethod
	def get_all_islands(cls):
		return cls.total_islands
	
		
class Trainer:
	def __init__(self,name):
		
		self._food_in_bag=0
		self._experience=100
		self._name=name
		self._current_island=None  #taking an attribute of none type
		self._max_food_in_bag=10*(self._experience)
		self.pokemon_list=[]
		
		
	@property
	def name(self):
		return self._name
		
	@property
	def food_in_bag(self):
		return self._food_in_bag
	
	@property
	def experience(self):
		return self._experience
	
	@property
	def max_food_in_bag(self):
		return self._max_food_in_bag
	
	@property
	def current_island(self):
		if(self._current_island==None):            #giving safe accesss
			print("You are not on any island")
		else:
			return self._current_island
			
	def move_to_island(self,island):
		self._current_island = island
	
	def collect_food(self):
		if self._current_island==None:
			print("Move to an island to collect food")
		else:
			if self._current_island._total_food_available_in_kgs>self._max_food_in_bag:
				if self._food_in_bag<self._max_food_in_bag:
					self._current_island._total_food_available_in_kgs-=self._max_food_in_bag
					self._food_in_bag+=self._max_food_in_bag
				else:
					self._food_in_bag=self._max_food_in_bag
			else:
				self._food_in_bag=self._current_island._total_food_available_in_kgs
				self._current_island._total_food_available_in_kgs=0
                
	def catch(self,pokemon):
		pokemon._master=self
		if  self._experience>=100*pokemon.level:
			print("You caught {}".format(pokemon.name))
			self._experience+=20
			self.pokemon_list.append(pokemon)
		else:
			print("You need more experience to catch {}".format(pokemon.name))
			
			
	def get_my_pokemon(self):
		return self.pokemon_list
		
