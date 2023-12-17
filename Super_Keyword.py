class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

Rd = Employee("RD", "5260")
Ydik = Programmer("Ydik", "2345", "Python")
print(Ydik.name)
print(Ydik.id)
print(Ydik.lang)