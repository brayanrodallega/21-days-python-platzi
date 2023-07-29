'''
En este desafío, debes crear una jerarquía de clases mediante el uso de la herencia.

La clase base será Animal con las propiedades name, age y specie y un método getInfo que devuelve un objeto con la información del animal.

Luego, debes crear una clase Mammal que herede de Animal y tenga una propiedad adicional hasFur y un método getInfo que sobreescriba al del padre y incluya la información de hasFur.

Finalmente, debes crear una clase Dog que herede de Mammal y tenga una propiedad adicional breed y un método getInfo que sobreescriba al del padre y incluya la información de breed, al igual que el método bark que devuelva el string "woof!". Las propiedades de specie y hasFur deben estar incluídas como "dog" y True respectivamente desde la implementación por lo que no debe ser necesario pasar los valores a la hora de crear la instancia.

Ejemplo 1

Input:
bird = Animal("pepe", 1, "bird")
bird.getInfo()

Output:

{
  "name": "pepe",
  "age": 1,
  "specie": "bird",
}

Ejemplo 2

Input:
hippo = Mammal("bartolo", 3, "hippo", false)
hippo.getInfo()

Output:

{
  "name": "bartolo",
  "age": 3,
  "specie": "hippo",
  "hasFur": false,
}

Ejemplo 3

Input:
dog = Dog("fido", 4, "pastor aleman");
dog.bark()

Output:
"woof!"
'''

# Solución:

class Animal:
    def __init__(self, name, age, specie):
        self._name = name
        self._age = age
        self._specie = specie

    def getInfo(self):
       return {
           "name": self._name,
           "age": self._age,
           "specie": self._specie
       }
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    @property
    def specie(self):
        return self._specie
    
    @specie.setter
    def specie(self, specie):
        self._specie = specie
    
  
class Mammal(Animal):
    def __init__(self, name, age, specie, has_fur):
        super().__init__(name, age, specie)
        self._has_fur = has_fur

    def getInfo(self):
        return {
           "name": self._name,
           "age": self._age,
           "specie": self._specie,
           "hasFur": self._has_fur
        }

    @property
    def has_fur(self):
        return self._has_fur
    
    @has_fur.setter
    def has_fur(self, has_fur):
        self._has_fur = has_fur
    

class Dog(Mammal):
    def __init__(self, name, age, breed ):
        super().__init__(name, age, "dog", True)
        self._breed = breed
        
    def bark(self):
        return "woof!"

    def getInfo(self):
        return {
           "name": self._name,
           "age": self._age,
           "specie": self._specie,
           "hasFur": self._has_fur,
           "breed": self._breed
        }
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        self._breed = breed



bird = Animal("pepe", 1, "bird")
print(bird.getInfo())

hippo = Mammal("bartolo", 3, "hippo", False)
print(hippo.getInfo())

dog = Dog("fido", 4, "pastor aleman");
print(dog.bark())