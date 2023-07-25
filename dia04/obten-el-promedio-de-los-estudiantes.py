'''
En este desafío, deberás calcular el promedio general de una clase, así como el promedio individual de cada estudiante.

Para ello, se te proporcionará una lista de diccionarios, cada uno de los cuales representará a un estudiante y tendrá las siguientes propiedades:

"name": El nombre del estudiante
"grades": Las notas de cada materia del estudiante
A partir de esta información, debes retornar un nuevo diccionario que tenga la propiedad "class_average" con el promedio de la clase y una lista de "students" con los estudiantes y sus promedios individuales.

Es importante mencionar que los promedios deben ser calculados con precisión y se deben redondear a dos decimales para que los test pasen sin problema alguno. Puedes usar el método round() el cual se usa de la siguiente manera 👇

number = 100.32433
number = round(number, 2)

# 100.32

Ejemplo:


Input: get_student_average([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
])

Output: {
  "class_average": 88.17,
  "students": [
    {
      "name": "Pedro",
      "average": 88.75
    },
    {
      "name": "Jose",
      "average": 88.5
    },
    {
      "name": "Maria",
      "average": 87.25
    }
  ]
}
'''

# Solución:

def get_student_average(students):

    class_average = 0
    students_list = []
    
    for student in students:
        student_name = student["name"]
        student_grades = student["grades"]
        student_average = sum(student_grades) / len(student_grades)
        student_average = round(student_average, 2)
    
        class_average += student_average
    
        students_list.append({
        "name": student_name,
        "average": student_average,
        })
    
    class_average = class_average / len(students)
    class_average = round(class_average, 2)
    
    return {
        "class_average": class_average,
        "students": students_list,
    }
    pass
