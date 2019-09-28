class Hero:
	def __init__(self,name,health,armor):
		self.name = name
		self.health = health
		self.armor = armor

class hero_intelegnt(Hero):
	def __init__(self,name):
		super().__init__(name, 100,90)


lina = hero_intelegnt("lina")

print(lina.name," ", lina.health,lina.armor)
