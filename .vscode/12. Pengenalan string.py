import os
os.system('cls')

### Pengenalan string
## A. Cara membuat string
print('\rA). Cara membuat string')
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''
data = 'menggunakan single quote'
print(data)
data = "menggunakan double quote"
print(data)

print("'Halo apa kabar?'") #quote di dalam quote
print('"Halo apa kabar?"') #quote di dalam quote
print("ini hari jum'at\n") #ini bisa


## B. Menggunakan tanda dalam string
print('\nB). Menggunakan tanda dalam string')
# membuat tanda ' menjadi string
print('mari salat jum\'at')
print('g\'day, isn\'t it?')
# backslash
print('C:\\user\\ucup') #menggunakan double backslash agar backslash dapat muncul di string
# tab
print('ucup\tganteng') #membuat tab dalam string
# backspace
print('ucup \bganteng') #menghapus jarak dalam string
# newline
print('baris pertama. \nbaris kedua.') # LF --> line feed --> digunakan di OS : unix, mac os, linux
print('baris pertama. \rbaris kedua.') # CR --> carriage return --> digunakan di OS : commodore, acorn, lisp
print('baris pertama. \n\rbaris kedua') # CRLF --> line feed carriage return --> digunakan di OS : windows

print('')
print('')


## C. String literal atau RAW
print('C). String literal atau RAW')

print('C:\new folder') #hati-hati ini ini akan salah path-nya
# kita dapat menggunakan :
#1. raw string
print(r'C:\new folder') #apapun yang berada di dalam tanda quote setelah 'r' akan menjadi string 

#2. multiline literal string
print('''
Nama: Fauzan ganteng
Kelas: 11 SD
Website: www.ojanganteng.com
      ''') #dalam string ini, "enter" akan dideteksi juga

#3. multiline literal string dan RAW
print(r'''
Nama: Fauzan ganteng \n
Kelas: 11 \r SD
Website: www.ojanganteng.com
      ''') #tanda \n dan \r tidak akan dideteksi sebagai enter
