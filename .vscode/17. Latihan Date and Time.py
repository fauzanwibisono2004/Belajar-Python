import os
os.system('cls')

### Date and Time
import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f'today is = {hari_ini:%A}\n') #"%A" untuk menampilkan hari berdasarkan tanggal

tanggal_lahir = dt.date(2004,11,5)
print(f'Tanggal lahir Fauzan Wibisono : {tanggal_lahir}')
#penulisan tanggal, bulan, dan tahun harus dalam tipe integer.

## Input user
print("\nSilahkan masukkan tanggal, bulan, dan tahun lahir anda ")
tanggal = int(input('Tanggal \t: '))
bulan = int(input('Bulan \t\t: '))
tahun = int(input('Tahun \t\t: '))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f'tanggal lahir anda yaitu, {tanggal_lahir}')
print(f'harinya adalah {tanggal_lahir:%A}\n')

## Menghitung umur
print("===== Menghitung Umur =====\nSilahkan masukkan tanggal, bulan, dan tahun lahir anda ")
tanggal = int(input('Tanggal \t: '))
bulan = int(input('Bulan \t\t: '))
tahun = int(input('Tahun \t\t: '))
tanggal_lahir = dt.date(tahun,bulan,tanggal)

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365 #".days" berguna untuk mengambil hari/days nya saja dari hasil pengurangan tanggal kalender
#kita menggunakan operasi "//" agar hasil perhitungan tidak koma dan akan bertipe integer
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f'umur anda saat ini adalah = {umur_tahun} tahun, {umur_bulan_sisa} bulan.\n')

