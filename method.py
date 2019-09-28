class hero:
	#class variabel/inherintance
	jumlah = 0

	def __init__(self,name,darah,armor):
		self.name = name
		self.darah =darah
		self.armor = armor

	#method tanpa return dan tanpa  argument

	def kondisi(self):
		print("ini adalah hero",self.name)

	#method dengan argument

	def healthup(self,up):
		self.darah += up

	#method dengan retrun 

	def gethealth(self):
		return self.darah

hero1 = hero("hayabusa",20,5)
hero1.kondisi()#harus pakai (), ini adalah hero hayabusa
hero1.healthup(20)
print(hero1.gethealth())# 40 harus di print karean ini return