## Membuat gabungan area rentang dari angka
'''
- not (not)
- or (or)
- and (and)
- xor (^)

'''
# Buatlah logika matematika dengan menggunakan operator logika 'or' dan 'and' :
#diberikan rentang angka 3 sampai 10 :
## 1. Operator "OR" (gabungan angka)
print('\n=======OR=======')
#rentang angka x < 3 , x > 10
# +++++++3-------10+++++++
print('+++++++3-------10+++++++')
inputUser = float(input('Masukkan angka : '))

x_kurang_dari_3 = (inputUser < 3)
print('x < 3 :',x_kurang_dari_3)
x_lebih_dari_10 = (inputUser > 10)
print('x > 10 :',x_lebih_dari_10,'\n')

gabungan = x_kurang_dari_3 or x_lebih_dari_10
print('Nilai gabungan : ',gabungan,'\n')

## 2. Operator "AND" (irisan angka)
print('=======AND=======')
#rentang angka 3 < x < 10
# -------3+++++++10-------
print('-------3+++++++10-------')
inputUser = float(input('Masukkan angka : '))

x_lebih_dari_3 = (inputUser > 3)
print('x > 3 : ',x_lebih_dari_3)
x_kurang_dari_10 = (inputUser < 10)
print('x < 10 : ',x_kurang_dari_10,'\n')

irisan = x_lebih_dari_3 and x_kurang_dari_10
print('Nilai irisan : ',irisan,'\n')
print('')


## TUGAS 
print('===========TUGAS===========')

# 1. ------0++++++5------8+++++++11------
print('1. ------0++++++5------8+++++++11------\n  0 < x < 5  or  8 < x < 11  adalah')
inputUser = float(input('Masukkan angka : '))

satu = inputUser > 0
dua = inputUser < 5
tiga = inputUser > 8
empat = inputUser < 11

antara_0_dan_5 = (satu and dua)
antara_8_dan_11 = (tiga and empat)

hasil = antara_0_dan_5 or antara_8_dan_11
print('hasilnya : ',hasil,'\n')

# 2. ++++++0------5++++++8------11++++++
print('2. ++++++0------5++++++8------11++++++\n  x < 0  or  5 < x < 8  or  x > 11  adalah')
inputUser = float(input('Masukkan angka : '))

satu = inputUser < 0
dua = inputUser > 5
tiga = inputUser < 8
empat = inputUser > 11

antara_5_dan_8 = dua and tiga

hasil = satu or antara_5_dan_8 or empat
print('hasilnya : ',hasil,'\n')


## jadii,,,
# Dalam pengodingan python interval matematika, kita membuat persyaratan untuk "x >" dan "x <" (x lebih/kecil dari)
# Kita menggunakan "and" apabila x berada dalam interval irisan dua objek
# Kita menggunakan "or" apabila x yang berada dalam interval dua objek saling bergabung 