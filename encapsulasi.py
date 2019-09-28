#encapsulasi adalah cara untuk mengubah semua menjadi variabel 
#private yang aka menjadi terbagi dua yaitu getter dan setter
# getter adalah mengambil variabel
# setter adalah menseting variabel

class hero:

	def __init__(self,name,health):
		self.__nama = name
		self.__health = health

	# getter
	# mengkonversikan agar private bisa di akses

	def getname(self):
		return self.__nama

	def gethealth(self):
		return self.__health

	# setter
	def diserang(self,serang):
	 	self.__health -= serang

hero1 = hero("hayabusa",20)

print(hero1.getname())
hero1.diserang(5)
print(hero1.gethealth())# 15