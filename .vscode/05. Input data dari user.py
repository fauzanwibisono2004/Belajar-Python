import os
os.system('cls')

## Cara mengambil input dari user :
print("Bebas mau masukin angka atau kalimat")
data = input("Masukkan data input : ")
print("data output :",data," bertipe ",type(data))
# Pada output yang keluar, data akan selalu bertipe string. String bisa huruf
print("")

# Bila kita ingin merubah tipe data output, maka caranya :
# 1.) string --> integer
print("Masukkan angka! (bukan koma)")
data_int = int(input("Masukkan data input : "))
print("data output : ",data_int," bertipe ",type(data_int))
print("")

# 2.) string --> float
print("Masukkan angka! (boleh koma)")
data_float = float(input("Masukkan data input : "))
print("data output :",data_float," bertipe ",type(data_float))
print("")

## Bagaimana dengan data boolean? (boolean = biner)
# untuk mengubah data string ke boolean, kita perlu mengubah dulu ke integer. 
# jadi urutanya akan seperti ini, string --> integer --> boolean
# 3.) string --> boolean
print("data biner hanya 1 atau 0")
biner = bool(int(input("Masukkan data boolean : ")))#jika user memasukkan angka != 0, hasil boolean akan selalu "True"
print("data output :",biner," bertipe",type(biner))
print("")

