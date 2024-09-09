### Kalkulator Sederhana

print('====== Kalkulator Sederhana ======')
angka_1 = float(input('Masukkan angka = '))
operator = input('Operator ( + , - , * , / )  : ')
angka_2 = float(input('Masukkan angka = '))

## Percabangannya 
if operator=='+' :
    hasil = angka_1 + angka_2
    print(f'Hasilnya = {hasil}')
elif operator=='-' :
    hasil = angka_1 - angka_2
    print(f'Hasilnya = {hasil}')
elif operator=='*' :
    hasil = angka_1 * angka_2
    print(f'Hasilnya = {hasil}')
elif operator=='/' :
    hasil = angka_1 / angka_2
    print(f'Hasilnya = {hasil}')
else :
    print('Operator tidak terdaftar')
    
print('\nTerimakasih !!\n')