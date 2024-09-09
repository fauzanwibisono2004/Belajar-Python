### Format string

#sebelumnya kita tau :
nama = 'Fauzan'
string = 'Hallo '+nama+' apa kabar?'
print(string)

#contoh tersebut ribet dan panjang
#kita bisa gunakan format string 
## contoh generic :
# String
nama = 'Fauzan'
format_string = f'Hallo {nama} apa kabar?'
print(format_string)

# Angka 
angka = 2004.5 #tipe datanya float
format_string = f'nilai angkanya = {angka}' #kita tidak perlu lagi merubah tipe data float menjadi string untuk melakukan print
print(format_string)

# Boolean
boolean = False
format_string = f'nilai boolean = {boolean}'
print(format_string)

# Bilangan bulat
angka = 15
format_string = f'nilai bilangan bulat = {angka:d}'
print(format_string)

# Bilangan dengan ribuan 
angka = 2000000
format_string = f'nilai jutaan = {angka:,}'
print(format_string)

# Bilangan desimal
angka = 2004.54321
format_string = f'nilai desimal = {angka:.2f}' #keterangan ".2f" artinya kita hanya mengambil dua angka di belakang koma
print(format_string)

# Menampilkan leading zeroo
angka = 2004.54 #total indeksnya adalah 7
format_string = f'nilainya = {angka:8}' #angka 8 di situ artinya menambahkan indeks yang semula ada 7 bertambah 1 indeks di depan angka
print(format_string)
#contoh lain agar lebih terlihat :
angka = 2004.54 #total indeksnya adalah 7
format_string = f'nilainya = {angka:08}' # angka 0 mengisi indeks yang baru ditambahkan
print(format_string)

# Menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f'minus = {angka_minus}'
format_plus = f'plus = {angka_plus:+}' #agar tanda '+' muncul, kita menambahkan "+" 
print(format_minus)
print(format_plus)

# Memformat persen
persentase = 0.045
format_persen = f'persentase = {persentase:%}' #merubah angka desimal menjadi persentase
print(format_persen)
#contoh lain agar angka di belakang koma dibatasi :
persentase = 0.045
format_persen = f'persentase = {persentase:.2%}' #".2%" artinya kita membatasi dua angka di belakang koma
print(format_persen)

# Melakukan operasi aritmatika
harga = 10000
jumlah = 5
format_string = f'harga total = Rp{jumlah*harga:,}'
print(format_string)

format_string = f'harga total = Rp{harga*jumlah:,}' #dibalik pun tidak masalah
print(format_string)

# Format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hex = {hex(angka)}'

print(format_binary)
print(format_octal)
print(format_hex)
