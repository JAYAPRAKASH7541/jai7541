class Animal:
    sound_by_animal=""
    make_breathe=""
    feed_grow=0
    hunt_animal=""
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        if age_in_months !=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        if required_food_in_kgs <=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
        self._breed=breed
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    
    @classmethod
    def breathe(cls):
        print(cls.make_breathe)
    
    @classmethod
    def make_sound(cls):
        print(cls.sound_by_animal)
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.feed_grow    
        
        
    def hunt(self,zoo):
        if "Deer" not in zoo.total_animals:
            print("No deers to hunt")
        else:
            zoo.total_animals.remove(self.hunt_animal)
            zoo.total_animals-=1
        
            
            
class Deer(Animal):
    sound_by_animal="Buck Buck"
    make_breathe="Breathe in air"
    feed_grow=2
    
    
class Lion(Animal):
    sound_by_animal="Roar Roar"
    make_breathe="Breathe in air"
    feed_grow=4
    hunt_animal="Deer"
    
    
    
class Shark(Animal):
    sound_by_animal="Shark Sound"
    make_breathe="Breathe oxygen from water"
    feed_grow=8
    
    
    
class GoldFish(Animal):
    sound_by_animal="Hum Hum"
    make_breathe="Breathe oxygen from water"
    feed_grow=0.2
    
class Snake(Animal):
    sound_by_animal="Hiss Hiss"
    make_breathe="Breathe in air"
    feed_grow=0.5
    hunt_animal="Deer"
    
    
class Zoo:
    def __init__(self):
        self._reserved_food_in_kgs=0
        self.total_animals=[]
        
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs

    def add_food_to_reserve(self,food_amount):
        self._reserved_food_in_kgs+=food_amount
        
        
    def add_animal(self,animal):
        self.total_animals.append(animal)
        
    def feed(self,animal):
        feed_required = animal._required_food_in_kgs
        if self._reserved_food_in_kgs >= feed_required:
            animal.grow()
            self._reserved_food_in_kgs -= feed_required
     
    def count_animals(self):
        return (len(self.total_animals))
        
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        pass
    
    @staticmethod
    def count_animals_in_given_zoos():
        pass
    
    
    
    
    
    
    
#zoo= Zoo()
#zoo.add_food_to_reserve(10000000)
#lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
#zoo.add_animal(lion)
#nehru_zoological_park.count_animals()
#Zoo.count_animals_in_all_zoos()
#Zoo.count_animals_in_given_zoos([zoo])
#zoo.total_animals

# >>> from zoo import Deer
# >>> deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
# >>> nehru_zoological_park.add_animal(deer)
# >>> nehru_zoological_park.count_animals()
# 2
# >>> lion.hunt(nehru_zoological_park)
# >>> nehru_zoological_park.count_animals()
# 1
# >>> lion.hunt(nehru_zoological_park) # Prints
# No deers to hunt
# '''