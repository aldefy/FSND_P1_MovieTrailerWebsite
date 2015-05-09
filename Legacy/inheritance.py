class Parent(object):
  """docstring for Parent"""
  def __init__(self, last_name, eye_color):
    self.last_name = last_name
    self.eye_color = eye_color

class Child(Parent):
  """docstring for Child"""
  def __init__(self, last_name, eye_color, number_of_toys):
    Parent.__init__(self, last_name, eye_color)
    self.number_of_toys = number_of_toys

child = Child("X", "Black", 100)
print(child.last_name)
print(child.eye_color)
print(child.number_of_toys)
