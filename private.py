#private > rahasia
#protected > terlindungi

class hero:

	def __init__(self,name,health):
		self.name = name
		self.health = health

		#variabel instance private
		self.__privated = "rahasia"

		#variabel instance protected
		self._protected = "terlindungi"

hero1 = hero("nana",20)
print(hero1._protected)# hasil terlindungi
hero1._protected = "mengubah"

hero1.__privated = "diubah"#harus di deklarasikan agar bisa di akses
print(hero1.__privated)

hero1.name = "layla"# mengubah

print(hero1.name)# di ubah name
hero1.name = 3# mengubah ke integer
print(hero1.name)