class murid:
	jurusan = "tkj"

	def __init__(self,nama,umur):
		self.nama = nama
		self.umur = umur

	def belajar(self):
		print("sedang belajar")

	def belajar2(self,kondisi):
		print(self.name,"belajar",kondisi)

bento = murid("bentoss",18)
davin = murid("kuswara",19)
bento.jurusan = "rpl"#instance variabel,mengubah hanya untuk    tertentu

#print(bento.nama)
print(davin.jurusan)#tkj
print(bento.jurusan)#rpl
print(bento.__dict__)
print(bento.belajar)

