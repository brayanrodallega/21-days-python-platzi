"""
Tu objetivo es crear una clase llamada MyList que simule el comportamiento de una Lista nativa en Python, sin utilizar los métodos ya existentes. Implementarás la lógica de los siguientes métodos:

map(func): itera sobre cada elemento de nuestra estructura aplicando la función func a cada uno de ellos y devuelve una nueva lista (que será una instancia de MyList).

filter(func): itera sobre cada elemento de nuestra estructura filtrándolos según lo que indique la función func y devuelve una lista con los elementos filtrados (también una instancia de MyList).

join(character): concatena todos los elementos de nuestra estructura de datos en un string, separándolos por el carácter indicado (character). Si no se proporciona un carácter, el separador por defecto será una coma ",".

append(item): agrega un elemento item al final de la lista y aumenta la longitud (length).

pop(): elimina el último elemento de la lista y lo retorna, disminuyendo también la longitud (length).

shift(): elimina el primer elemento de la lista y lo retorna, disminuyendo la longitud (length).

unshift(item): agrega un elemento item al inicio de la lista y aumenta la longitud (length).

Además, deberás almacenar los elementos dentro de la propiedad data y el número de elementos dentro de la propiedad length, para que puedan ser consultados desde las pruebas.

Ejemplo 1:

Input:

myList = MyList()
myList.append("a")
myList.append("b")
myList.append("c")

print(myList.data)

Output:

{0: 1, 1: 2, 2: 3}

Ejemplo 2:

Input:

myList = MyList()
myList.append("Platzinauta")
myList.unshift("Hola!")

print(myArray.data)

Output:
{0: "Hola!", 1: "Platzinauta"}
"""

# Solución:

class MyList:
    def __init__(self):
        self.data = {}
        self.length = 0

    def append(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        element = None
        if self.data != {}:
            element = self.data[self.length - 1]
            del self.data[self.length - 1]
            self.length -= 1
        return element

    def shift(self):
        element = None
        if self.data != {}:
            element = self.data[0]
            del self.data[0]
            self.data = {item - 1: value for item, value in self.data.items()}            
            self.length -= 1
        return element

    def unshift(self, item):
        if self.data != {}:
            aux = {0: item}
            for item, value in self.data.items():
                aux[item + 1] = value
            self.data = aux
            self.length += 1

    def map(self, func): 
        payload = MyList.__new__(MyList)
        payload.data = {}
        payload.length = self.length
        for item, value in self.data.items():
            payload.data[item] = func(value)
        return payload if payload else None

    def filter(self, func):
        payload = MyList.__new__(MyList)
        payload.data = {}
        payload.length = 0
        for item, value in self.data.items():
            if func(value):
                payload.data[payload.length] = value
                payload.length += 1
        return payload if payload else None

    def join(self, character = ','):
        string = ''
        if self.data != {}:
            for key, value in self.data.items():
                if key == self.length-1:
                    string += f'{value}'
                else:
                    string += f'{value}{character}'
        return string


# Input:

# myList = MyList()
# myList.append(1)
# myList.append(2)
# myList.append(3)
# myList.append(4)
# myList.append(5)
# myList.append(6)


# print(myList.data)
# print(myList.shift())
# print(myList.data)
# myList.unshift(7)
# print(myList.data)
# print(myList.map(lambda x: x*2).data)
# print(myList.filter(lambda x: x != 1).data)
# print(myList.join('$'))

# ismap = (myList.map(lambda x: x*2))
# print(isinstance(ismap, MyList))
# isfilter = (myList.filter(lambda x: x != 2))
# print(isinstance(isfilter, MyList))


# Output:

# {0: 1, 1: 2, 2: 3}

# Ejemplo 2:

# Input:

# myList = MyList()
# myList.append("Platzinauta")
# myList.unshift("Hola!")

# print(myList.data)

# Output:
# {0: "Hola!", 1: "Platzinauta"}
