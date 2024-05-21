
n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    
    data_aplikasi[nama_kategori] = aplikasi

print(data_aplikasi)

daftar_aplikasi_list = [set(aplikasi) for aplikasi in data_aplikasi.values()]


hasil_intersection = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil_intersection = hasil_intersection.intersection(daftar_aplikasi_list[i])

print("Aplikasi yang ada di semua kategori:", hasil_intersection)

satukategori = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    satukategori = satukategori.symmetric_difference(daftar_aplikasi_list[i])
print("Aplikasi yang hanya ada di satu kategori:", satukategori-hasil_intersection)


duakategori = set()

for i in range(len(daftar_aplikasi_list) - 1):
     hasil = (daftar_aplikasi_list[i].intersection(daftar_aplikasi_list[i+1])).difference(satukategori)
     duakategori.union(hasil)
hasil2 = (daftar_aplikasi_list[0].intersection(daftar_aplikasi_list[-1])).difference(satukategori)
duakategori.union(hasil2)
print("Aplikasi yang muncul tepat di 2 kategori: ", duakategori)
