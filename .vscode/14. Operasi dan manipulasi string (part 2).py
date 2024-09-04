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
print('======= Pengecekan dengan menggunakan isX method =======')
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

judul = 'Deadpool Vs Wolverine'
cek_judul = judul.istitle() #tipa datanya boolean
print(judul,' is title =',str(cek_judul)) #hasilnya "True" karena memang benar dalam penulisan "Deadpool VS Wolverine" semua kata diawali kapital
judul = 'Deadpool Vs wolverine'
cek_judul = judul.istitle() #tipa datanya boolean
print(judul,' is title =',str(cek_judul)) #hasilnya "False" karena ada satu huruf depan judul yang tidak kapital."
print('')


## Mengecek komponen "startswith()" dan "endswith()"


