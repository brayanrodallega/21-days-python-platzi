'''
En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.

Recibirás una lista de diccionarios que incluirán las siguientes propiedades:

"name": nombre del gatito.
"followers": una lista de números, donde cada uno representa los seguidores de cada red social.
Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores. Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante, manteniendo el orden en el que aparecen en la lista de entrada.

Tendrás inputs y outputs como los siguientes 👇

Ejemplo 1:


Input: find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
])

Output: ["Luna"]

Ejemplo 2:


Input: find_famous_cat([
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
])

Output: ["Milo", "Gizmo"]
'''

# Solución:

def find_famous_cat(cats):
  
  famous = []
  fmax = 0
  
  for cat in cats:
    total_followers = 0
    for follower in cat["followers"]:
      total_followers += follower
    if (total_followers > fmax):
      fmax = total_followers
      if (len(famous) != 0):
        famous.pop()
      famous.append(cat["name"])
    elif total_followers == fmax:
      famous.append(cat["name"])
        
  return famous
  pass