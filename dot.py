"""
class mahasiswa:
	nama = "terserah"

otong = mahasiswa
ucup = mahasiswa

otong.nama = "otong serutup"
ucup = "michel ucup"

print(otong.nama)#otong serutup
"""
"""
class murid:
	jurusan = "tkj"

	def __init__(self,name,age,departement):
		self.nama = name
		self.umur = age
		self.jurusan = departement


murid1 = murid("bento",17,"rpl")
murid2 = murid("Davin",18,"tkj")

print(murid1.jurusan)
murid1.hobi = "membaca"#menambah instance variabel
print(murid1.hobi)#membaca
print(murid2.jurusan)#tkj
murid2.jurusan = "ips"
print(murid2.jurusan)#ips
murid1.nama = 123#mengubah string menjadi integer
print(murid1.nama)#123
"""
"""
#turunan
class bapak(object):

	def __init__(self,name,work):
		self.nama = name
		self.pekerjaan = work

	def kondisi(self):
		print("berjalan kedepan")

class anak(bapak):
	pass

class1 = bapak("manihuruk","petani")
class2 = anak("bento","pelajar")

print(class2.nama)#bento
print(class1.nama,class1.pekerjaan)
class1.kondisi()#berjalan kedepan,tidak usa pakai print,karena di def sudah di print
class2.kondisi()
"""
"""
#constructorinit
class hero:
	jumlah = 0

	def __init__(self,name,blood):
		self.nama = name
		self.darah = blood

		hero.jumlah += 1

hero1 = hero("layla",20)
print(hero1.jumlah)#1
hero2 = hero("zilong",30)
print(hero1.jumlah)#2
print(hero2.jumlah)#2
"""
"""
#method
class hero:
	jumlah = 0 

	def __init__(self,name,health,armor):
		self.nama = name
		self.kesehatan = health
		self.baja = armor

	#method tanpa return,tanpa argument
	def kondisi(self):
		print("ini adalah hero",self.nama)

	#method dengan argument
	def kondisi2(self,up):
		self.kesehatan += up

	# method dengan return
	def kondisi3(self):
		return self.kesehatan

hero1 = hero("hayabusa",30,5)

hero1.kondisi()#ini adalah hero hayabusa  , uda diprint di def
hero1.kondisi2(40)
print(hero1.kondisi3())# 70  di print karena return
"""
#private dan protected variabel
"""
class hero:
	jumlah = 0

	def __init__(self,name,health):
		self.nama = name
		self.kesehatan = health
	# variabel private
		self.__rahasia = "agen"
	#variabel protected
		self._terlindungi = "aman"

hero1 = hero("zilong",100)
print(hero1._terlindungi)# aman , ia bisa langsung di akses tanpa harus di deklarasikan terlebih dahulu
hero1.__rahasia = "siap"#deklarasikan dahulu agar bisa di akses, atau juga bisa di ubah isi variabel nya
print(hero1.__rahasia)#siap
hero1._terlindungi = 90 # mengubah isi variabel
print(hero1._terlindungi)#90
"""
#encapsulasi , mengubah semua menjadi varaibel private
#menggunakan setter dan getter
"""
class hero:
	def __init__(self,name,health):
		self.__nama = name
		self.__kesehatan = health

	#getter 
	def getname(self):
		return self.__nama

	#getter 
	def gethealth(self):
		return self.__kesehatan

	#setter 
	def diserang(self,serang):
		self.__kesehatan -= serang

hero1 = hero("layla",40)

print(hero1.getname())# layla
# itu lah gunanya return agar variabel private nya bisa akses tanpa di deklarasikan lagi
hero1.diserang(20)
print(hero1.gethealth())# 20
"""
"""
class cek:
	def __init__(self,name,age):
		self.nama = name
		self.umur = age

	def kondisi(self,kata):
		print(self.nama,"sedang",kata)
ben = cek("bento",17)
ben.kondisi("belajar")
#bento sedang belajar
"""

# setter dan getter python
# @property menjadikan method/fungsi menjadi variabel
"""
class hero:
	def __init__(self,name,health,armor):
		self.name = name
		self.__health = health
		self.__armor = armor
		self.__info = self.name,self.__health,self.__armor

	@property
	def cek(self):
		return self.__info


	@property 
	def armor(self):
		pass

	@armor.getter 
	def armor(self):
		return self.__armor

	@armor.setter
	def armor(self,input):
		self.__armor = input

sniper = hero("onehero",200,20)
print(sniper.cek)

print(sniper.armor)
sniper.armor = 90
print(sniper.armor)
	



class hero:

	def __init__(self,name,age):
		self.nama = name
		self.__age = age
		self.__info = self.nama,self.__age

	@property
	def cek(self):
		return self.__info
	@property
	def age(self):
		pass

	@age.getter
	def age(self):
		return self.__age
	@age.setter
	def age(self,input):
		self.__age = input

hero1 = hero("zilong",10)
print(hero1.cek)
print(hero1.cek)
hero1.age = 90
print(hero1.age)"""
"""
class hero:

	def __init__(self,name,age):
		self.nama = name
		self.__umur = age
	

	@property 
	def umur(self):
		pass

	@umur.getter
	def umur(self):
		return self.__umur
	@umur.setter
	def umur(self,input):
		self.__umur = input

hero1 = hero("layla",90)

print(hero1.umur)#90
hero1.umur = 100
print(hero1.umur)#100"""

#inheritance
"""
class hero:#super class

	def __init__(self,name,health):
		self.nama = name
		self.kesehatan = health

class hero1(hero):#subclass
	pass

class hero2(hero):
	pass

sniper = hero("layla",90)
sniper1 = hero1("lesley",100)
sniper2 = hero2("miya",80)

print(sniper.nama)#layla
print(sniper1.nama)#lesley
print(sniper2.nama)#miya
"""
#superclass
# dalam pemrograman usahkan jangan pernah melakukan looping atau pengulangan
#ini lah gunanya inhiretance/pewarisan
"""
class heroek:
	def __init__(self,name,health):
		self.nama = name
		self.health = health

	def info(self):
		print("ini adalah hero",self.nama)

class sniper(heroek):
	def __init__(self,nama):# gunannya mengambil ulang atau mendeklarasikan ulang kembali dari superclass
		#heroek.__init__(self,nama,200)#self/nama nya berasal dari init di atas bukan dari superclass
		super().__init__(nama,200)
		#super yang dimaksud adalah superclass dari heroek yang telah dideklarasikan di atas
		#.__init__adalah isi dari heroek dan untuk nama dan health

class fighter(heroek):
	def __init__(self,nama):
		#hero.__init__(self,nama,300)
		super().__init__(nama,90)
		super().info()

hero1 = sniper("zilong")
hero2 = fighter("layla")
print(hero1.nama)#zilong
print(hero1.health)#200
print(hero2.nama)#layla
print(hero2.health)#300

"""
#override method /menyampingkan fungsi
#usahkan untuk nama class huruf besar
"""
class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def showinfo(self):#walaupun di hapus tidak mengapa di bawah,kalau pun ada akan di timpa dengan showinfo yang kedua
		print("ini showinfo superclass")
		print("{} health:{}".format(self.name,self.health))

class hero_biasasaja(Hero):
	def __init__(self,name):
		super().__init__(name,200)# ini adalah mengambil dari superclass


	def showinfo(self):
		print("ini showinfo subclass")
		print("{} \n\ttipe:biasa saja, \n\thealth:{}".format(self.name,self.health))# ini menimpah
class hero_luarbiasa(Hero):
	def __init__(self,name):
		super().__init__(name,100)# ini adalah mengambil dari superclass

lina = hero_biasasaja("lina")
axe = hero_luarbiasa("axe")

lina.showinfo()#akan mengambil showinfo yang kedua dan menimpa showinfo superclass
# hasil
ini showinfo subclass
lina 
	tipe:biasa saja, 
	health:200

axe.showinfo()# karena untuk class luarbiasa belum ada showinfo,jadi mengambil dari atas/induk
#hasil 
ini showinfo superclass
axe health:100"""
# multipe inheritance
"""
class A:
	def method_A(self):
		print("ini adalah method A")

class B:
	def method_B(self):
		print("ini adalah method B")

class C(A,B):
	pass

kondisi = C()

kondisi.method_A()# ini adalah method A
kondisi.method_B()#ini adalah metod B """
"""
#multipe inheritance
class Team:

	def setTeam(self,team):
		self.team = team

	def showTeam(self):
		print(self.team)

class Tipe:

	def setTipe(self,tipe):
		self.tipe = tipe

	def showTipe(self):
		print(self.tipe)
	def oke(self):
		print("okea")

class Hero(Team,Tipe):

	def __init__(self,name,health):
		self.name = name
		self.health = health

hero1 = Hero("ucup",90)

hero1.setTeam("pssp")
hero1.setTipe("gelandang")

hero1.showTeam()#pssp
hero1.showTipe()#gelandang"""
"""
#method resulation order // multipe inheritance
# bagaimana jika def/method yang  penamaannya sama dan mana yang akan lebih dahulu d panggil
# dan yang di panggil adalah sesuai urutan, contoh jika class c(a,b)maka a dahulu di panggil jika nama def sama
# atau jika class c(b,a)maka b yang di print
class A:
	def show(self):
		print("ini adalah method a")

class B:
	def show(self):
		print("ini adalah method b")

class C(A,B):
	jika class c(B,A),maka yang akan di baca b 
	pass
	#def show(self):# ini akan lebih dahulu diekseusi jika di panggil => objek.show
		print("ini adalah method c")
objek = C()
objek.show()# yang keluar ini adalah method a , karena method a akan di eksekusi dulu
# karena class C pass, jika di C di buat def maka itu akan luan di eksekusi
#help(objek)# untuk cek mana yang lebih luan dieksekusi"""
"""
# diamond problem
class A:
	def show(self):
		print("ini adalah class a")
 
class B(A):
	def show(self):
		print("ini adalah class b")

class C(A):
	def show(self):
		print("ini adalah class c")

class D(B,C):
	def show(self):
		print("ini adalah class d")

objek = D()

objek.show()# ini adalah class d
#jika,"saya buat class dan semua yang seharus nya huruf besar menjadi huruf kecil agar lebih cepat"
#class c(b,c) dan pass, maka, object show(),hasilnya adalah dari show b, dan jika show b di hapus/class b pass , maka
# dari show dari class c dan jika juga di hapus , maka show dari class a,
# help(objek)untuk detail lihat"""

# magic method
# __init__ salah satunya , dan masi banyak lagi cari contoh nya,
"""
class Pisang:

	def __init__(self,name,harga):
		self.name = name
		self.harga = harga

	def __repr__(self):# ada di bug
		return "ini adalah buah {}".format(self.name)
		# jika def repr gk ada dan di print(objek),maka hasil nya <__main__.Pisang object at dst)
		# repr akan membuat ini adalah buah pisang, pisang berasal dari format self.name

	def __str__(self):
		return "ini adalah buah nya {}".format(self.name)

	@property# harus buat ke property dulu jika __dic__
	def __dict__(self):
		return " ini adalah dict yang terbaca"

objek = Pisang("barangan",10)
objek1 = Pisang("ambon",20)
#print(objek)# jika ada repr nya maka hasiln nya ini adalah buah barangan
print(objek1)# ini adalah buah nya ambon, itu karena str terbaca dan repr gk , j
# repr dan str sama saja, perbedaanya repr ada di bug,jika ada str maka di yang akan di ekseusi repr enggak,
#untuk mengakses nya
print(repr(objek1))# ini adalah buah ambon, karena sudah di buat ke repr
print(objek1.__dict__)# ini adalah dict yang terbaca"""
# abstrak class
from abc import ABC,abstracmethod

class Button(ABC):

	@abstracmethod
	def click(self):
		pass

class PushButton(Button):

	def click(self):
		print("push button click")
tombol1 = PushButton()

tombol1.click()
help(tombol1)