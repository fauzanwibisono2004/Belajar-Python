import os
os.system('cls')

# Superclass / Kelas Induk
class hero :
    def __init__(self,name,health) :
        self.name = name
        self.health = health

# Subclass dari Kelas Induk
class hero_intelligent(hero) :
    def __init__(self,name) :
        hero.__init__(self,name,100)
class hero_strenght(hero) :
    def __init__(self,name) :
        hero.__init__(self,name,200)

# Objek
lina = hero_intelligent('lina')
axe = hero_strenght('axe')

print(lina.name,' ',lina.health)
print(axe.name,' ',axe.health)
print('\n')






# CARA LAIN
print('--------- CARA LAIN ---------')
# Superclass / Kelas Induk
class hero :
    def __init__(self,name,health) :
        self.name = name
        self.health = health

# Subclass dari Kelas Induk
class hero_intelligent(hero) :
    def __init__(self,name,health) :
        super().__init__(name, health) #Kalo di sini mau nambahin variabel "health", maka __init__ subclass-nya juga harus ditambah variabel "health"
class hero_strenght(hero) :
    def __init__(self,name) :
        super().__init__(name, 200)

# Objek
lina = hero_intelligent('lina',230)
axe = hero_strenght('axe')

print(lina.name,' ',lina.health)
print(axe.name,' ',axe.health)
print('\n')

