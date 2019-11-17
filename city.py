class person():
	def __init__(self,name,age,city,gender,food,fav_place):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
		self.food=food
		self.fav_place=fav_place
	def eating(self):
		print(self.name+" is eating "+ self.food)
	def go_out(self):
		print(self.name+" likes to go "+self.fav_place)
yazan=person("yazan",15,"jerusalem","boy","everything","football field")
yazan.eating()
yazan.go_out()



