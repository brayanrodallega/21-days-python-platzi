class PatientNode:
  def __init__(self, name, age, bed):
    self.name = name
    self.age = age
    self.bed = bed
    self.next = None

  def retorno(self):
    return {'name': self.name, 'age': self.age, 'bedNumber': self.bed}
