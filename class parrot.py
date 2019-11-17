class Animal(object):
	def __init__(self,sound,name,age,favorit_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.favorit_color=favorit_color
	def eat(self,food):
		print("yummy!!"+self.name+"is eating"+food)
	def description(self):
		print(self.name+"is"+self.age+"years old and loves the color"+self.favorite_color)
	def make_sound(self):
		for i in range (3):
			print("the sound is "+self.sound)
lion=Animal("roar","lion",23,"green")
lion.make_sound()
