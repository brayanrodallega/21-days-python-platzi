'''
En este desafío, debes crear la lógica de la función find_words_with_two_vowels que encuentre las palabras que contienen exactamente dos vocales en una lista de palabras. Las vocales pueden ser tanto mayúsculas como minúsculas.

Recibirás un único parámetro: una lista de palabras. La función debe devolver una nueva lista que contenga todas las palabras de la lista original que cumplan con la condición mencionada anteriormente. En caso de no haber palabras que cumplan con esta condición deberás retornar una lista vacía.

Ejemplo 1:

Input: find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
])

Output: ["hello", "platzi"]

Ejemplo 2:

Input: find_words_with_two_vowels(["text", "test", "python", "example"])
Output: []
'''

# Solución:

def find_words_with_two_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    words_vowels = [word for word in words if sum(word.count(vowel) for vowel in vowels) == 2]
    return words_vowels
    pass