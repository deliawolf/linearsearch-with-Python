##NIM   : 10116068
##NAMA  : aditya mr

##fungsi pencarian dengan liniersearch
def linearSearch(item,my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position] == item:
            found = True
        position = position + 1
    return found

    
kotak = ['book','pencil','pen','note book','sharpener','rubber']
isikotak = input('masukan barang ke kotak! ')
while not isikotak:
    isikotak = input('masukan barang ke kotak! ')

#isikotak dimasukan ke list kotak posisi 0(awal)
kotak.insert(0, isikotak)

#memberikan perintah cari isi kotak tanpa validasi kosong dan memanggil item dari fungsi liniersearch
item = input('cari barang apa di kotak? ')

#memanggil fungsi linierSearch di list
itemFound = linearSearch(item,kotak)

#memeriksa ketersediaan barang di kotak
if itemFound:
    print ('ya ini barang yang dicari')
else:
    print ('maaf sekali, barang tidak ada di dalam kotak')

#menampilkan semua barang di kotak
print ('barang di box ada :')
print (' '.join(map(str, kotak)))