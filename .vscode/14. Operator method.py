import os
os.system('cls')

### Operator dalam bentuk methods

## Merubah case dari string
print('======= Merubah case pada string =======')
# Merubah semua huruf ke uppercase (Merubah jadi kapital)
salam = 'bro!'
print('normal =',salam)

salam = salam.upper() #kata "bro!" akan menjadi kapital semua
print('upper =',salam)

# Merubah semua huruf ke lowercase (Merubah jadi huruf kecil)
kenalan = 'AKU FAUZAN'
print('normal =',kenalan)

kenalan = kenalan.lower()
print('lower =',kenalan)
print('')


## Pengecekan dengan menggunakan isX method
print('====== Pengecekan dengan menggunakan isX method ======')
#Contoh untuk pengecekan lower case :
salam = 'anjay'
print('kata :',salam)

apakah_lower = salam.isupper() #tipe datanya boolean. Untuk mengecek apakah kapital atau huruf kecil
print(salam,'is upper =',str(apakah_lower))

apakah_lower = salam.islower() #tipe datanya boolean. Untuk mengecek apakah kapital atau huruf kecil
print(salam,'is lower =',str(apakah_lower),'\n')
#Artinya, program dapat mengenali bahwa kata "anjay" ditulis dalam huruf kecil.

# "isalpha()" ---> untuk mengecek semua huruf
# "isalnum()" ---> untuk mengecek huruf dan angka
# "isdecimal()" ---> untuk mengecek angka saja
# "isspace()" ---> mengecek spasi, tab, newline \n
# "istitle() ---> semua kata yang dimulai dengan huruf kapital

# Pengecekan huruf awalan judul apakah sudah kapital
judul = 'Deadpool Vs Wolverine'
cek_judul = judul.istitle() #tipe datanya boolean
print(judul,' is title =',str(cek_judul)) #hasilnya "True" karena memang benar dalam penulisan "Deadpool VS Wolverine" semua kata diawali kapital

judul = 'Deadpool Vs wolverine'
cek_judul = judul.istitle() #tipa datanya boolean
print(judul,' is title =',str(cek_judul)) #hasilnya "False" karena ada satu huruf depan judul yang tidak kapital."
print('')


## Mengecek komponen "startswith()" dan "endswith()"
print('==== Mengecek komponen "startswith()" dan "endswith()" ====')
#Diberikan kalimat :
nama = 'Fauzan Wibisono'
print(nama)

# 1. Cek kata pertama dalam kalimat  
cek_start = nama.startswith('Fauzan') #tipe datanya boolean
print('start \"Fauzan\" =',str(cek_start))
# 2. Cek kata terakhir dalam kalimat
cek_end = nama.endswith('Wibisono') #tipe datanya boolean
print('end \"Wibisono\" =',str(cek_end))
print('')


## Penggabungan komponen join() dan split()
# Penggabungan menggunakan "join()"
susunan = ['aku','sayang','kamu'] #ini adalah list
print(susunan)
#lalu kita gabungkan dari list tersebut :
gabung = ' aw '.join(susunan)
print(gabung)
gabung = ' '.join(susunan)
print(gabung,"\n")

# Pemisahan menggunakan "split()" 
#"split()" adalah kebalikan dari "join()"
susunan = 'akuawsayangawkamu'
print(susunan)

print(susunan.split('aw'),'\n') #dia akan menghilangkan "aw" dan kembali lagi menjadi list
print('')


## Alokasi karakter rjust(), ljust(), center()
print('===== Alokasi karakter rjust(), ljust(), center() =====')

align_kanan = 'kanan'.rjust(20) #20 adalah jumlah index dalam string
print('|'+align_kanan+'|') #akan di posisikan di paling kanan
#jika di dalam print menggunakan "+", dia akan menambahkan tanpa memberikan "spasi" 
align_kiri = 'kiri'.ljust(20)
print('|'+align_kiri+'|')
align_center = 'center'.center(20)
print('|'+align_center+'|\n')

#atau bisa juga seperti ini :
align_kanan = 'kanan'.rjust(20,'*') #tanda koma setelah angka 20 berguna untuk menyisipkan simbol / string lain
print('|'+align_kanan+'|') 
align_kiri = 'kiri'.ljust(20,'*')
print('|'+align_kiri+'|')
align_center = 'center'.center(20,'*')
print('|'+align_center+'|')

# Kebalikannya, yaitu --> strip() untuk menghilangkan suatu karakter tertentu
align_center = align_center.strip('*') #artinya kita ingin menghilangkan "*" yang ada pada align_center sebelumnya 
print('|'+align_center+'|')