import os
os.system('cls')

## Tipe data yang ada di python :
# 1. Angka yang tidak ada koma (integer)
data_int = 1
print("data : ",data_int)
print("bertipe : ",type(data_int)) 
#penulisan lainnya bisa seperti di bawah ini :
print("data : ",data_int,", bertipe :",type(data_int)) 

print(" ")#(sebagai spasi baris)

# 2. Angka koma (float)
data_float = 2.5
print("data : ",data_float)
print("bertipe :",type(data_float))
#penulisan lainnya dapat seperti di bawah ini :
print("data :",data_float,", bertipe :", type(data_float))

print(" ")#(spasi baris)

# 3. Kumpulan karakter (string). Bisa huruf, angka, angka koma
data_str = "Fauzan"
print("data :",data_str)
print("bertipe :",type(data_str))

print(" ")

# 4. Biner true/false (boolean)
data_bool = True
print("data :",data_bool)
print("bertipe :",type(data_bool))

print(" ")#(spasi baris)

## Tipe data khusus :
# Bilangan kompleks
data_complex = complex(5,6) #"j" adalah bilangan kompleks
print("data :",data_complex)
print("bertipe :",type(data_complex))

print(" ")

# Tipe data dari bahasa C (double, char, long)
from ctypes import c_double #e.g: import 'double' dari C
data_c_double = c_double(10.5)
print("data :",data_c_double)
print("bertype :",type(data_c_double))

print(" ")






