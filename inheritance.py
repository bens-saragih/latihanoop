class bapak(object):

	def __init__(self,name,work):
		self.nama = name
		self.pekerjaan = work

	def berjalan(self):
		print("berjalan")


class anak(bapak):#inheritance/warisan
	pass

b = bapak("manihuruk","petani")
a = anak("bento","pelajar")

print(b.nama,b.pekerjaan)#manihuruk petani
print(a.pekerjaan)#pelajar
b.berjalan
