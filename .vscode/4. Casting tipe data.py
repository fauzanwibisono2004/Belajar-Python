# Casting adalah merubah dari satu tipe data ke tipe data yang lain
# misalkan :
print("=======INTEGER=======")
# Sebuah data integer,
data_int = 92
print("data :",data_int)
print("type :",type(data_int))
print(" ")

# Operator casting untuk merubah tipe data, contoh, 
# Integer to float :
data_float = float(data_int)
print("data :",data_float)
print("tipe :",type(data_float))
print(" ")
# Integer to string :
data_str = str(data_int)
print("data :",data_str)
print("tipe :",type(data_str))
print(" ")
# Integer to bool :
data_bool = bool(data_int)
print("data :",data_bool) #akan "false" jika integer = 0
print("tipe :",type(data_bool))
print(" ")


print("=======FLOAT=======")
# Sebuah data Float,
data_float = 2.8
print("data :",data_float," bertipe ",type(data_float))

# Merubah float to integer, string, boolean :
data_int = int(data_float)#akan dibulatkan ke bawah
data_str = str(data_float)
data_bool= bool(data_float)#akan false jika nilai float = 0
print("data :",data_int," bertipe ",type(data_int))
print("data :",data_str," bertipe ",type(data_str))
print("data :",data_bool," bertipe ",type(data_bool))
print(" ")


print("=======BOOLEAN=======")
# Sebuah data Boolean
data_bool = True
print("data :",data_bool," bertipe ",type(data_bool))

# Merubah boolean to integer, float, string :
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data :",data_int," bertipe ",type(data_int))
print("data :",data_float," bertipe ",type(data_float))
print("data :",data_str," bertipe ",type(data_str))
print(" ")


print("=======STRING=======")
# Sebuah data String
data_str = "Fauzan"
print("data :",data_str," bertipe ",type(data_str))

# Merubah string to integer, float, boolean :
data_int = int(data_str)#data string huruf tidak dapat diubah menjadi integer, kecuali bila data string berupa angka
data_float = float(data_str)
data_bool = bool(data_str)#data boolean akan berubah menjadi "false" apabila data string kosong (data_str = "")
print("data :",data_int," bertipe ",type(data_int))
print("data :",data_float," bertipe ",type(data_float))
print("data :",data_bool," bertipe ",type(data_bool))
print(" ")
