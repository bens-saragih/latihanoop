class hero:
	jumlah = 0

	def __init__(self,name,kekuatan,darah):
		#instance variabel
		self.nama = name
		self.kekuatan = kekuatan
		self.darah = darah
		hero.jumlah += 1

	def eak(self,kondisi):
		print(self.nama,"belajar di",kondisi)


hero1 = hero("zilong",30,5)
#harus langsung di bawah object biar keluar 1&2
print(hero1.jumlah)#1
hero2 = hero("layla",25,10)
print(hero2.jumlah)#2
hero1.eak("kelas")#zilong belajar di kelas