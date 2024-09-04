### Operasi dan manipulasi string
## 1. Menyambung string (concatenate)
print('==== 1. Menyambung string (concatenate) ====')
nama_depan = 'Fauzan' 
nama_tengah = 'Wibisono'
nama_belakang = 'Ganteng'

nama_lengkap = nama_depan + ' ' + nama_tengah + ' ' + nama_belakang
print('Nama lengkap :',nama_lengkap)
print('')


## 2. Menghitung panjang string (length)
print('==== 2. Menghitung panjang string (length) ====')
panjang = len(nama_lengkap) #tipe datanya menjadi integer
print('panjang dari',nama_lengkap,'=', str(panjang)) #huruf dan spasi terdeteksi juga. tipe data dikembalikan menjadi string
print('')


## 3. Operator untuk string
print('==== 3. Operator untuk string ====')
# Mengecek apakah ada komponen char atau string pada string. Hanya mengecek ada atau tidak
a = 'a'
cek = a in nama_lengkap #tipe datanya menjadi boolean
print(a,'ada di',nama_lengkap,'=',str(cek)) #tipe data dikembalikan menjadi string

a = 'Ganteng'
cek = a in nama_lengkap #tipe datanya menjadi boolean
print(a,'ada di',nama_lengkap,'=',str(cek),) #tipe data dikembalikan menjadi string

a = 'Ganteng'
cek = a not in nama_lengkap #not in adalah kebalikan dari in
print(a,'ada di',nama_lengkap,'=',str(cek),) 

# Mengulang string 
print('HA'*5)
print(5*'WK') #bisa juga dibalik

# Indexing
nama_lengkap = "Fauzan Wibisono Ganteng"
print('index ke-0 =',nama_lengkap[0]) #index dalam string selalu dimulai dari 0
print('index ke-1 =',nama_lengkap[1])
print('index ke-(-1) =',nama_lengkap[-1]) #apabila minus, maka akan diambil dari char yang paling belakang
print('index ke-(-2) =',nama_lengkap[-2]) 
print('index ke-[0:3] =',nama_lengkap[0:3]) #asumsi mengambil karakter F,a,u,z tapi ternyata tidak. Hanya F,a,u
#dalam python, jika ingin mengambil range data, maka index data terakhir tidak ikut serta sehingga perlu ditambah satu angka
#contoh :
print('index ke-[0:3] =',nama_lengkap[0:4]) # [0 : 4] sehingga didapat char F,a,u,z
print('index ke-[0,2,4,6,10] =',nama_lengkap[0:11:2]) #angka 2 sebagai increment (kenaikan), akan didapat char : F,u,a,(spasi),i,i
print('')


## 4. Operator dalam bentuk method 
print('==== 4. Operator dalam bentuk method ====')
nama = 'Fauzan Wibisono'
jumlah = nama.count('o') #untuk menghitung jumlah char pada string. Tipe datanya adalah integer
print('jumlah huruf o pada',nama,'=',str(jumlah),'\n')


#### Selanjutnya akan membahas lebih lanjut mengenai method.....