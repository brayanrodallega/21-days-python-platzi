'''
En este desafío, vamos a implementar una lista enlazada simple para almacenar información sobre pacientes de un hospital. Cada nodo de la lista representará a un paciente y tendrá los siguientes campos:

    Nombre del paciente (cadena de texto)
    Edad del paciente (número)
    Número de cama asignada al paciente (número)

La lista enlazada deberá tener los siguientes métodos:

    addPatient(name, age): agrega un nuevo paciente a la lista, asignándole la próxima cama disponible. Si no hay camas disponibles, debe lanzar un error con el mensaje "No hay camas disponibles".

    removePatient(name): remueve al paciente con el nombre especificado de la lista y libera su cama. Si el paciente no se encuentra en la lista, debe lanzar un error con el mensaje "Paciente no encontrado".

    getPatient(name): retorna la información del paciente con el nombre especificado en el siguiente formato {name, age, bedNumber}. Si el paciente no se encuentra en la lista, debe lanzar un error con el mensaje "Paciente no encontrado".

    getPatientList(): retorna una lista con la información de todos los pacientes en la lista, cada paciente deberá tener el siguiente formato {name, age, bedNumber}.

    getAvailableBeds(): retorna un número con el total de camas disponibles.

Recuerda usar la sintaxis raise Exception("mensaje") para lanzar errores.

Aquí tienes un ejemplo de cómo se utilizaría esta singly linked list:


list = PatientList(3)
list.addPatient("Paciente 1", 20)
list.addPatient("Paciente 2", 30)

list.getPatientList()

Output:

[
  { 'name': 'Paciente 1', 'age': 20, 'bedNumber': 1 },
  { 'name': 'Paciente 2', 'age': 30, 'bedNumber': 2 },
]

list.getPatient("Paciente 1")

Output:

{ 'name': 'Paciente 1', 'age': 20, 'bedNumber': 1 }

list.removePatient("Paciente 1")

list.getPatientList()

Output:

[
  { 'name': 'Paciente 2', 'age': 30, 'bedNumber': 2 },
]
'''

# Solución:

from node import PatientNode

class PatientList:

    def __init__(self, max_beds):
        self.head = None
        self.tail = None
        self.length = 0
        self.max_beds = max_beds
        self.beds = {bed: True for bed in range(1, max_beds + 1)}

    def bed_available(self):
        bed = next((bed for bed in self.beds if self.beds[bed]), None)
        self.beds[bed] = False
        if bed is None:
            raise Exception("No hay camas disponibles")
        return bed

    def addPatient(self, name, age):
        bed = self.bed_available()
        new_node = PatientNode(name, age, bed)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def removePatient(self, name):
        if self.head is None:
            return
        if self.head.name == name:
            self.beds[self.head.bed] = True
            self.head = self.head.next
            self.length -= 1
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.name == name:
                self.beds[current_node.next.bed] = True
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next

    def getPatient(self, name):
        current_node = self.head
        while current_node:
            if current_node.name == name:
                return current_node.retorno()
            current_node = current_node.next
        if current_node is None:
            raise Exception("Paciente no encontrado")


    def getPatientList(self):
        patiens = []
        current_node = self.head
        while current_node:
            patiens.append(current_node.retorno())
            current_node = current_node.next
        return patiens

    def getAvailableBeds(self):
        return self.max_beds - self.length

    def get_beds(self):
        return self.beds



list = PatientList(3)
list.addPatient("Paciente 1", 20)
list.addPatient("Paciente 2", 30)

patients = list.getPatientList()
print(patients)

list.removePatient("Paciente 1")

patients = list.getPatientList()
print(patients)

list.addPatient("Paciente 3", 50)
list.addPatient("Paciente 4", 40)
list.addPatient("Paciente 5", 70)

patients = list.getPatientList()
print(patients)

beds = list.get_beds()
print(beds)

# patient = list.getPatient("Paciente 2")
# print(patient)

print(list.getAvailableBeds())