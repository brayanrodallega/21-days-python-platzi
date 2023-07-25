'''
En este desafío, implementarás la lógica de un planificador de tareas en Python. El objetivo es construir la función closure llamada createTaskPlanner, que devolverá una serie de métodos para administrar las tareas. A continuación, se detallan los métodos que deben implementarse:

addTask(task): recibe un diccionario que contiene la información de la tarea y la agrega al array de tareas. El diccionario debe contener las siguientes claves: 'id', 'name', 'priority', 'tags' y 'completed'. La clave 'completed' se establecerá automáticamente como False al agregar una tarea.

removeTask(value): recibe el id o nombre de la tarea y la elimina del array de tareas.

getTasks(): devuelve el array de tareas.

getPendingTasks(): devuelve solo las tareas pendientes.

getCompletedTasks(): devuelve solo las tareas completadas.

markTaskAsCompleted(value): recibe el id o nombre de la tarea y la marca como completada.

getSortedTasksByPriority(): devuelve una copia de las tareas ordenadas según su prioridad (3: poco urgente, 2: urgente, 1: muy urgente), sin modificar la lista original de tareas.

filterTasksByTag(tag): filtra las tareas por una etiqueta específica. updateTask(taskId, updates): busca la tarea correspondiente al id especificado y actualiza sus propiedades con las especificadas en el diccionario de actualizaciones.

Ejemplo 1:

Input:

planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

planner['markTaskAsCompleted']('Llamar a Juan')

print(planner['getCompletedTasks']())

Output:

[{
  'id': 2,
  'name': 'Llamar a Juan',
  'completed': True,
  'priority': 3,
  'tags': ['personal']
}]

Ejemplo 2:


Input:
planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

print(planner['filterTasksByTag']('shopping'))

Output:

[{
    'id': 1,
    'name': 'Comprar leche',
    'completed': False,
    'priority': 1,
    'tags': ['shopping', 'home']
}]
'''

# Solución:

def createTaskPlanner():

    tasks = []

    def addTask(task):
        task['completed'] = False
        tasks.append(task)
        pass

    def removeTask(value):
        for task in tasks:
            if value == task['id'] or value == task['name']:
                tasks.remove(task)
                break
        pass

    def getTasks():
        return tasks
        pass

    def getPendingTasks():
        return [task for task in tasks if task['completed'] == False]
        pass

    def getCompletedTasks():
        return list(filter(lambda x: x['completed'] == True, tasks))
        pass

    def markTaskAsCompleted(value):
        for task in tasks:
            if value == task['id'] or value == task['name']:
                task['completed'] = True
                break
        pass

    def getSortedTasksByPriority():
        return sorted(tasks, key=lambda x: x['priority'])
        pass

    def filterTasksByTag(tag):
        return list(filter(lambda x: tag in x['tags'], tasks))
        pass

    def updateTask(taskId, updates):
        for task in tasks:
            if task['id'] == taskId:
                task.update(updates)
                break
        pass

    return {
        'addTask': addTask,
        'removeTask': removeTask,
        'getTasks': getTasks,
        'getPendingTasks': getPendingTasks,
        'getCompletedTasks': getCompletedTasks,
        'markTaskAsCompleted': markTaskAsCompleted,
        'getSortedTasksByPriority': getSortedTasksByPriority,
        'filterTasksByTag': filterTasksByTag,
        'updateTask': updateTask
    }