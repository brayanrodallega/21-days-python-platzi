## 🐍 Aprende a leer archivos de texto y CSV en Python 📂

La lectura de archivos en Python es fundamental para el procesamiento de datos. Aquí tienes un resumen de cómo hacerlo:

### Leer archivos de texto:

Abre el archivo en modo lectura: ``file = open("archivo.txt", "r")``
Lee todo el contenido: ``content = file.read()``
Lee línea por línea:

```python
line = file.readline()
while line:
    print(line)
    line = file.readline()
```

Lee todas las líneas y almacénalas en una lista: ``lines = file.readlines()``

Recuerda cerrar el archivo con ``file.close()`` y usa bloques ``try-finally`` o ``with`` para garantizar el cierre correcto.

### Leer archivos CSV:

Importa el módulo csv: ``import csv``
Abre el archivo CSV en modo lectura: ``with open('archivo.csv', 'r') as file:``
Crea un objeto lector CSV: ``csv_reader = csv.reader(file)``
Lee las filas del archivo CSV con un bucle for:

```python
for row in csv_reader:
    # Accede a los valores de cada columna en la fila
    print(row)
```

Leer datos en diccionarios (si hay encabezados):

```python
with open('archivo.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Accede a los valores utilizando los nombres de las columnas
        print(row['columna1'], row['columna2'])
```

Recuerda que los archivos CSV pueden tener diferentes delimitadores, que se especifican con el parámetro ``delimiter``.

¡Aprende más en el Curso de Python: Comprehensions, Funciones y Manejo de Errores! 🚀 #Python #DataProcessing #CSV

[Enlace al Curso](https://platzi.com/cursos/python-funciones/)