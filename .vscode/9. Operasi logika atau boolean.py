## Operasi logika atau boolean
# Ada beberapa operasi logika atau boolean, yaitu :
'''
- not (not)
- or (or)
- and (and)
- xor (^)

'''

## NOT (untuk membalik/berlawanan nilai statement)
print('=======NOT=======')
print('untuk membalik/berlawanan nilai statement')
#diberikan variabel :
a = True
b = not a
print('data a =',a)
print('--- NOT ---')
print('data b =',b,'\n')

## OR (jika salah satu bernilai True, maka hasilnya adalah True)
print('=======OR=======')
print('jika salah satu bernilai True, maka hasilnya adalah True')
#diberikan soal :
# 1.
a = True
b = True
c = a or b
print(a,'or',b,'=',c)
# 2.
a = True
b = False
c = a or b
print(a,'or',b,'=',c)
# 3.
a = False
b = True
c = a or b
print(a,'or',b,'=',c)
# 4.
a = False
b = False
c = a or b
print(a,'or',b,'=',c,'\n')


## AND (jika dua buah bernilai True, maka hasilnya adalah True)
print('=======AND=======')
print('jika dua buah bernilai True, maka hasilnya adalah True')
#diberikan soal :
# 1.
a = True
b = True
c = a and b
print(a,'and',b,'=',c)
# 2.
a = True
b = False
c = a and b
print(a,'and',b,'=',c)
# 3.
a = False
b = True
c = a and b
print(a,'and',b,'=',c)
# 4.
a = False
b = False
c = a and b
print(a,'and',b,'=',c,'\n')


## XOR (jika hanya salah satu bernilai True, maka hasilnya adalah True)
print('=======XOR=======')
print('jika hanya satu bernilai True, maka hasilnya adalah True. Jika keduanya sama, maka akan menjadi False')
#diberikan soal :
# 1.
a = True
b = True
c = a ^ b
print(a,'^',b,'=',c)
# 2.
a = True
b = False
c = a ^ b
print(a,'^',b,'=',c)
# 3.
a = False
b = True
c = a ^ b
print(a,'^',b,'=',c)
# 4.
a = False
b = False
c = a ^ b
print(a,'^',b,'=',c,'\n')