import os

### FILTER DATA NAMA MENGGUNAKAN LOOPING DAN IF ELSE
print('\n===== FILTER DATA NAMA MENGGUNAKAN LOOPING DAN IF ELSE =====')
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


'''Setelah seluruh data didapatkan, lalu dilakukan penyaringan untuk tinggi dan berat badan yang ditentukan oleh user'''


while True :
	os.system("cls")
	print(nama)

	# List kosong untuk menyimpan hasil filter
	terpilih = []

	print('\n\n========== CARI ORANG ==========')
	tinggi_badan = int(input('Tinggi badan (cm) :  > '))
	berat_badan = int(input('Berat badan (kg) :  > '))

	'''Setelah mendapatkan tinggi dan berat badan yang diinginkan oleh user, selanjutnya dilakukan penyaringan'''
	# Filter manual dengan loop :
	for orang in nama :
    		if orang[2] >= tinggi_badan and orang[3] >= berat_badan : #Kita dapat langsung menulis orang[2] karena
        		terpilih.append(orang[0])
    		else :
        		pass


	'''
    Kita dapat langsung menulis orang[2] karena konsep looping secara otomatis akan mengecek 
	indeks list dalam list untuk tinggi badan dalam list nama[0][2], nama[1][2], nama[3,2] begitu seterusnya 
	sampai seluruh data dalam list nama didentifikasi.
    '''

	## Menampilkan hasil filter
	print(f'''
Orang dengan tinggi badan lebih dari {tinggi_badan} cm dan berat badan lebih dari {berat_badan} kg :
==>''')

	print(terpilih,'\n')

	lanjut = input("lanjut atau tidak? (y/n) : ")
	if lanjut == "n" :
		break

print("Terimakasih")