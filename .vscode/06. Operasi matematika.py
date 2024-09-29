import os
os.system('cls')

# Beberapa operasi matematika yang perliu diketahui :
"""
- Operasi tambah +
- Operasi pengurangan -
- Operasi perkalian *
- Operasi pembagian /
- Operasi eksponen (pangkat) **
- Operasi modulus %
- Operasi floor division //

"""
# Modulus adalah angka sisa pembagian. Jika angka pembagi lebih besar dari angka terbagi, hasilnya adalah angka terbagi itu sendiri
# Floor division adalah kebalikan dari modulus, lalu dibulatkan ke bawah

# Memberi variabel
a = 12
b = 3

# Penjumlahan :
hasil = a + b
print(a,'+',b,'=',hasil)
# Pengurangan :
hasil = a - b
print(a,'-',b,'=',hasil)
# Perkalian :
hasil = a * b
print(a,'*',b,'=',hasil)
# Pembagian :
hasil = a / b
print(a,'/',b,'=',hasil)
# Eksponen (Pangkat) :
hasil = a ** b
print(a,'**',b,'=',hasil)
# Modulus : (sisa pembagian)
hasil = a % b
print(a,'%',b,'=',hasil)
# Floor division : (hasil bagi, tanpa menyertakan sisa)
hasil = a // b
print(a,'//',b,'=',hasil)


## Prioritas operasi (operational precedence)
# diberikan variabel
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*','(',z,'+',x,')','/',y,'-',y,'%',z,'//',x,'=', hasil)

# Jadi urutan prioritas operasinya adalah :
'''
    1. Tanda kurung ()
    2. Eksponen **
    3. Perkalian, pembagian, modulus, dan floor division. * / % //
    4. Penjumlahan dan pengurangan + -

'''


