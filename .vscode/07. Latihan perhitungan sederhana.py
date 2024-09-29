import os
os.system('cls')

# Latihan Konversi Satuan Temperature 
print("\nPROGRAM KONVERSI TEMPERATURE\n")

print('Konversi suhu celcius')
T_celcius = float(input('Besar temperatur dalam celcius : '))
print('')

# Celcius --> Reamur
Reamur = (4/5)*T_celcius
print('suhu dalam Reamur =',Reamur,'reamur')
# Celcius --> Fahrenheit
Fahrenheit = ((9/5)*T_celcius) + 32
print('suhu dalam Fahrenheit =',Fahrenheit,'fahrenheit')
# Celcius --> Kelvin
Kelvin = T_celcius - 273
print('suhu dalam Kelvin =',Kelvin,'kelvin \n')


## TUGAS :
# buatlah program untuk konversi suhu!
print('======= TUGAS =======')
# 1. Konversi nilai fahrenheit ke satuan suhu yang lain
print('1. Konversi nilai fahrenheit ke satuan yang lain \n')
T_fahrenheit = int(input('Besar suhu dalam fahrenheit : '))
print('')

Celcius = (5/9) * (T_fahrenheit - 32)
Reamur = (4/9) * (T_fahrenheit - 32)
Kelvin = (5/9 * (T_fahrenheit - 32)) + 273
print('suhu dalam celcius =',Celcius,'celcius')
print('suhu dalam reamur =',Reamur,'reamur')
print('suhu dalam kelvin =',Kelvin,'kelvin \n')

# 2. Konversi nilai kelvin ke satuan suhu yang lain
print('2. Konversi nilai kelvin ke satuan yang lain \n')
T_kelvin = int(input('Besar suhu dalam kelvin : '))
print('')

Celcius = T_kelvin - 273
Reamur = (4/5) * (T_kelvin - 273)
Fahrenheit = 9/5 * T_kelvin * (T_kelvin - 273) + 32
print('suhu dalam celcius =',Celcius,'celcius')
print('suhu dalam reamur =',Reamur,'reamur')
print('suhu dalam fahrenheit =',Fahrenheit,'fahrenheit \n')

