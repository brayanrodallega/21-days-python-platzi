'''
En este desafío deberás implementar la lógica de una función que cuente la cantidad de ocurrencias de cada letra en una cadena de texto y lo almacene en un diccionario.

Es importante mencionar que la función debe ser sensible a mayúsculas y minúsculas, es decir, las letras mayúsculas y minúsculas deben considerarse diferentes.

Ejemplo 1:


Input: "Hola mundo"

Output: {
  'H': 1,
  'o': 2,
  'l': 1,
  'a': 1,
  ' ': 1,
  'M': 1,
  'u': 1,
  'n': 1,
  'd': 1
}
'''

# Solución:

def count_letters(phrase):

    phrase_dic = {}

    for letter in phrase:
        phrase_dic[letter] = phrase_dic.get(letter, 0) + 1

    return phrase_dic
    pass