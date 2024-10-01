class Person:
    def __init__(self, name, age):
        self.__age = age  # Name mangling

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError("Age must be at least 18")
        self.__age = value

p = Person("John", 30)

# Akses melalui getter dan setter (terkontrol)
print(p.age)  # Output: 30
# atau
print(p._Person__age)  # Output: 30

# Akses langsung ke __age akan lebih sulit
try:
    print(p.__age)  # AttributeError: 'Person' object has no attribute '__age'
except AttributeError as e:
    print(e)
