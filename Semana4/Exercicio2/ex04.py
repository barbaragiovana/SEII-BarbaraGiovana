class Person:
  number_of_people = 0

  def __init__(self, name):
    self.name = name
    Person.add_person()

  @classmethod
  def get_number_of_people(cls):
    return cls.number_of_people
  
  @classmethod
  def add_person(cls):
    cls.number_of_people += 1

p1 = Person('Tim')
print(Person.number_of_people)
p2 = Person('Jill')
print(Person.number_of_people)
print(Person.get_number_of_people())

print(p1.number_of_people)
print(p2.number_of_people)
print(Person.number_of_people)

Person.number_of_people = 8
print(p1.number_of_people)
print(p2.number_of_people)
