##NIM   : 10116068
##NAMA  : aditya mr

#fungsi pencarian dengan linier search
def linearSearch(barang,list_kotak):
    #inisialisasi nilai found
	found = False
	#inisialisasi nilai posisi
	position = 0
	#perulangan  selama nilai posisi inisialisasi kurang dari posisi maximal kotak
	while position < len(list_kotak) and not found:
		#jika barang yang dicari ditemukan
		if list_kotak[position] == barang:
			found = True
		position = position + 1
	return found

#inisialisasi nilai ulangi
ulangi  = 'n'

#inisialisasi nilai list
kotak = ['buku 1','buku 2','buku 3']

#inisialisasi perulangan
ulangi = input('mau memasukan barang ke box (y / n)? ')
while not ulangi:
		ulangi = input('mau memasukan barang ke box (y / n)? ')
while ulangi == 'y':
		
	#menampilkan isi kotak
	print ('kotak berisi : ',', '.join(map(str, kotak)))
	print("\n")

	#perintah memasukan isi kotak
	isikotak = input('-masukan barang ke kotak! ')
	while not isikotak:
		isikotak = input('-masukan barang ke kotak! ')

	#isikotak dimasukan ke list kotak posisi 0(awal)
	kotak.insert(0, isikotak)

	#memberikan perintah cari isi kotak tanpa validasi kosong dan memanggil item dari fungsi liniersearch
	print("\n")
	barang = input('-cari ketersediaan barang apa di kotak? ')

	#memanggil fungsi linierSearch di list
	barangketemu = linearSearch(barang,kotak)

	#memeriksa ketersediaan barang di kotak
	if barangketemu:
		print ('barang '+barang+' ada di kotak' )
	else:
		print ('barang '+barang+' tidak ada di dalam kotak' )
	ulangi = input('mau memasukan barang ke box (y / n)? ')

#penghentian perulangan  
if ulangi == 'n':  
	print("\n")
	print ('batal memasukan barang')
