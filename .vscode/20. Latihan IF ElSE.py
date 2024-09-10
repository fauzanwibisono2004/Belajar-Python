### Kalkulator Sederhana

print('====== Kalkulator Sederhana ======')
angka_1 = float(input('Masukkan angka = '))
operator = input('Operator ( + , - , * , / )  : ')
angka_2 = float(input('Masukkan angka = '))

## Percabangannya 
if operator=='+' :
    hasil = angka_1 + angka_2
    print(f'Hasilnya = {hasil}')
elif operator=='-' :
    hasil = angka_1 - angka_2
    print(f'Hasilnya = {hasil}')
elif operator=='*' :
    hasil = angka_1 * angka_2
    print(f'Hasilnya = {hasil}')
elif operator=='/' :
    hasil = angka_1 / angka_2
    print(f'Hasilnya = {hasil}')
else :
    print('Operator tidak terdaftar')
    
print('\nTerimakasih !!\n')





### FILTER DATA NAMA HANYA MENGGUNAKAN IF ELSE
print('\n======= FILTER DATA NAMA HANYA MENGGUNAKAN IF ELSE =======')
'''
Nama : Fauzan Wibisono
NIM : 23/517493/PA/22186

Saya membuat list data nama lengkap dengan umur, tinggi badan, berat badan.
Saya membuatnya dengan menggunakan syntax List dan If Else Statement tanpa menggunakan looping. 
'''

# List berisi data orang dalam format [Nama, Umur, Tinggi Badan, Berat Badan]
nama = [
    ['Rayi', 19, 165, 55],
    ['Andika', 19, 170, 65],
    ['Zidan', 20, 165, 53],
    ['Rahma', 34, 160, 54],
    ['Aprilia', 19, 150, 49],
    ['Bagas', 19, 167, 53],
    ['Odi', 19, 178, 58],
    ['Fadil', 20, 171, 65],
    ['Bitring', 20, 169, 36],
    ['Bintang', 20, 165, 55],
    ['Andro', 20, 170, 60],
    ['Yudho', 22, 165, 56],
    ['Qonita', 20, 150, 45],
    ['Siti', 19, 150, 43],
    ['Rifalina', 30, 158, 48],
    ['Arsya', 20, 154, 50],
    ['Satria', 20, 165, 68],
    ['Nadilla', 19, 163, 56],
    ['Ananda', 20, 160, 59],
    ['Rico', 30, 165, 56]
]
print(nama)


# List kosong untuk menyimpan hasil filter
terpilih = []

'''Setelah seluruh data didapatkan, lalu dilakukan penyaringan untuk tinggi dan berat badan yang ditentukan oleh user'''

print('\n\n========== CARI ORANG ==========')
tinggi_badan = int(input('Tinggi badan (cm) :  > '))
berat_badan = int(input('Berat badan (kg) :  > '))

# Filter manual tanpa loop :
if nama[0][2] >= tinggi_badan and nama[0][3] >= berat_badan : #"nama[0][2]" artinya memanggil indeks list dalam list, yaitu memanggil tinggi badan. "nama[0][3]" memanggil indeks berat badan
    terpilih.append(nama[0][0]) 
else:
    pass
if nama[1][2] >= tinggi_badan and nama[1][3] >= berat_badan :
    terpilih.append(nama[1][0])
else:
    pass
if nama[2][2] >= tinggi_badan and nama[2][3] >= berat_badan :
    terpilih.append(nama[2][0])
else:
    pass
if nama[3][2] >= tinggi_badan and nama[3][3] >= berat_badan :
    terpilih.append(nama[3][0])
else:
    pass
if nama[4][2] >= tinggi_badan and nama[4][3] >= berat_badan :
    terpilih.append(nama[4][0])
else:
    pass
if nama[5][2] >= tinggi_badan and nama[5][3] >= berat_badan :
    terpilih.append(nama[5][0])
else:
    pass
if nama[6][2] >= tinggi_badan and nama[6][3] >= berat_badan :
    terpilih.append(nama[6][0])
else:
    pass
if nama[7][2] >= tinggi_badan and nama[7][3] >= berat_badan :
    terpilih.append(nama[7][0])
else:
    pass
if nama[8][2] >= tinggi_badan and nama[8][3] >= berat_badan :
    terpilih.append(nama[8][0])
else:
    pass
if nama[9][2] >= tinggi_badan and nama[9][3] >= berat_badan :
    terpilih.append(nama[9][0])
else:
    pass
if nama[10][2] >= tinggi_badan and nama[10][3] >= berat_badan :
    terpilih.append(nama[10][0])
else:
    pass
if nama[11][2] >= tinggi_badan and nama[11][3] >= berat_badan :
    terpilih.append(nama[11][0])
else:
    pass
if nama[12][2] >= tinggi_badan and nama[12][3] >= berat_badan :
    terpilih.append(nama[12][0])
else:
    pass
if nama[13][2] >= tinggi_badan and nama[13][3] >= berat_badan :
    terpilih.append(nama[13][0])
else:
    pass
if nama[14][2] >= tinggi_badan and nama[14][3] >= berat_badan :
    terpilih.append(nama[14][0])
else:
    pass
if nama[15][2] >= tinggi_badan and nama[15][3] >= berat_badan :
    terpilih.append(nama[15][0])
else:
    pass
if nama[16][2] >= tinggi_badan and nama[16][3] >= berat_badan :
    terpilih.append(nama[16][0])
else:
    pass
if nama[17][2] >= tinggi_badan and nama[17][3] >= berat_badan :
    terpilih.append(nama[17][0])
else:
    pass
if nama[18][2] >= tinggi_badan and nama[18][3] >= berat_badan :
    terpilih.append(nama[18][0])
else:
    pass
if nama[19][2] >= tinggi_badan and nama[19][3] >= berat_badan :
    terpilih.append(nama[19][0])
else:
    pass

## Menampilkan hasil filter
print(f'''
Orang dengan tinggi badan lebih dari {tinggi_badan} cm dan berat badan lebih dari {berat_badan} kg :
Format : [Nama, Umur, Tinggi Badan, Berat Badan]
==>''')

print(terpilih,'\n')
