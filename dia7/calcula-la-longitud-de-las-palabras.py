'''
En este desafío, debes crear una función llamada count_words_by_length que recibe una lista de palabras y devuelve un diccionario que mapea la longitud de las palabras a la cantidad de palabras que tienen esa longitud.

Ejemplo 1:

Input:
count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

Output:
{5: 2, 6: 2, 7: 1, 10: 1}

Ejemplo 2:

Input:
count_words_by_length([
  "apple",
  "banana",
  "orange"
])

Output:
{5: 1, 6: 2}
'''

# Solución:

def count_words_by_length(words):
    words_length = [len(word) for word in words]
    words_length_set = set(words_length)
    words_length_dict = {length: words_length.count(length) for length in words_length_set}
    return words_length_dict
    pass