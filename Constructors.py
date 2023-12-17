class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Banshee", "Developer")
b = Person("Ydik", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "Ydik"
# a.occ = "HR"
# a.info()
