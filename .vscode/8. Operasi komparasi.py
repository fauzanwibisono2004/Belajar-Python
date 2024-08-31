## Operasi komparasi
# Setiap hasil dari komparasi adalah boolean
# simbol komparasi : > , < , >= , <= , == , != , is , is not
'''
> : lebih dari
< : kurang dari
>= : lebih dari sama dengan
<= : kurang dari sama dengan
== : 'sama dengan'
!= : 'tidak sama dengan'
is : membandingkan memory/object (Variabel)
is not : 

'''
print('')
# diberikan variabel :
a = 3
b = 4

## kurang dari dan lebih dari (>,<)
hasil = a < b
print(a,'<',b,'=',hasil) 
hasil = a > b
print(a,'>',b,'=',hasil,'\n')


## sama dengan (==)
# Perbedaan "=" dengan "==" :
# = adalah assignment, sedangkan == adalah membandingkan
hasil = (a == 4)
print(a,'==',4,'=',hasil)
hasil = (a == 3)
print(a,'==',3,'=',hasil,'\n')


## "is" dan "is not" sebagai komparasi object identity
# Maksudnya adalah membandingkan dua variabel yang memiliki id atau address memory yang sama atau tidak
# misal, diberikan dua variabel serupa : 
a = 5
print('nilai a = 5 memiliki id =',hex(id(a)))
b = 5
print('nilai b = memiliki id =',hex(id(b)),)
hasil = a is b
print(a,'is',b,'=',hasil,'\n')
# Karena a dan b memiliki id atau address memory yang sama, maka hasilnya adalah True
# misal, dalam kasus false :
a = 5
print('nilai a = 5 memiliki id =',hex(id(a)))
b = 6
print('nilai b = 6 memiliki id =',hex(id(b)))
hasil = a is b
print(a,'is',b,'=',hasil,'\n')
# a dan b memiliki id atau address memory yang berbeda


