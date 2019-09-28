class hero:

	def __init__(self,name,health,armor):
		self.__name = name
		self.__health = health
		self.__armor = armor
		self.info = "name:{} \n\t health:{}".format(self.__name,self.__health)
		self.__info = "name:{} \n\t health:{}".format(self.__name,self.__health)

	def cek1(self):
		return "name:{} \n\t health:{}".format(self.name,self.health)

	@property
	def cek(self):
		return self.__info

	@armor.getter
	def armor(self):
		return self.__armor
		
	@armor.setter
	def armor(self):
		return self.__armor

hero1 = hero("dudung",20,10)
print(hero1.cek)

#membuat getter dan setter


print(hero1.armor)

