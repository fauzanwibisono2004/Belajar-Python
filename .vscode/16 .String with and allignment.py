## With and Multiline

# Data
data_nama = 'Fauzan Wibisono'
data_umur = 19
data_tinggi = 160
data_nomor_sepatu = 40

# String standard
data_string = f'nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, ukuran sepatu = {data_nomor_sepatu}' 
print('==== Data String =====')
print(data_string,'\n')

# String Multiline (dengan enter/newline/ "\n")
data_string = f'nama = {data_nama},\numur = {data_umur},\ntinggi = {data_tinggi},\nukuran sepatu = {data_nomor_sepatu}' 
print('==== Data String =====')
print(data_string)
print('')

# String multiline (dengan kutip triplets)
data_string = f"""
nama            = {data_nama}
umur            = {data_umur}
tinggi          = {data_tinggi}
ukuran sepatu   = {data_nomor_sepatu}
"""
print('\n==== Data String =====')
print(data_string)

#membuat agar hasilnya rata kanan (allignment)
data_string = f"""
nama            = {data_nama:>16}
umur            = {data_umur:>16}
tinggi          = {data_tinggi:>16}
ukuran sepatu   = {data_nomor_sepatu:>16}
"""
print('\n==== Data String =====')
print(data_string)
