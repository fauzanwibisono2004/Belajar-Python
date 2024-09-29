import os
os.system('cls')

# Operasi yang dapat dilakukan dengan penyingkatan (+= , -= , *= , /= , **= , %= , //=)
'''
Operasi yang dapat dilakukan penyingkatan :
    1. Operasi matematika
    2. Operasi bitwise
'''
#diberikan nilai a :
print('\ndiberikan nilai a = 5\n')

# Penjumlahan,
a = 5
a += 2
print('a + 2 = ',a)
# Pengurangan,
a = 5 #untuk mengembalikan nilai a = 5
a -= 2
print('a - 2 = ',a)
# Perkalian,
a = 5
a *= 2
print('a * 2 = ',a)
# Pembagian,
a = 5
a /= 2
print('a / 2 = ',a)
# Pangkat,
a = 5
a **= 2
print('a ** 2 = ',a)
# Modulus,
a = 5
a %= 2
print('a % 2 = ',a)
# Floor division,
a = 5
a //= 2 
print('a // 2 = ',a,'\n')