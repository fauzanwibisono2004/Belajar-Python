### ELIF = Else If statement

'''
    Alurnya :
    1. kondisi (True or False)
    2. Aksi
        3. Kondisi (True or False)
        4. Aksi
            5. Kondisi
            6. Aksi
'''

nama = input('Siapa namamu? ') #Input nama user

if nama=='ojan' : #Kondisi 1
    print('Halloo ojannn !!!!!') #Aksi true 1
elif nama=='romeo' : #Kondisi 2
    print('Hallo romeo !!!!!') #Aksi true 2
elif nama=='satria' : #Kondisi 3
    print('Hallo satriaa !!!!!') #Aksi true 3
else :
    print('oh maaf gak kenal') #Aksi false
    
print(f'Terimakasih yaa {nama}\n')