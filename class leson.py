# class people():
#     name = "John "
#     age = 28
#     height = 163.4
#
#     def sing(self):
#         print("lya lya lya")
#
#     def set_name(self, name):
#         self.name = name
#
# person1 = people()
# print(person1.name)
# print(person1.age)
# print(person1.height)
# print(type(person1))
# person1.sing()
# print(person1.name)
# person1.set_name("Narek")
# print(person1.name)
#
# print("____________________")
# class people():
#     name = None
#     age = None
#     height = None
#
#     def __init__(self, name, age, height):
#         self.set_name(name)
#         self.set_age(age)
#         self.set_height(height)
#         print("Constructor")
#
#     def sing(self):
#         print("lya lya lya")
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_age(self, age):
#         self.age = age
#
#     def set_height(self, height):
#         self.heght = height
#
#     def info(self):
#         print(f"Name in { self.name}\nAge is {self.age}\nHeight is {self.height}")
#
# student = people()
# student.set_name("Satenik")
# student.set_age(28)
# student.set_height(160)
# print(student.name)
#
# student2 = people()
# student2.set_name("Armen")
# student2.set_age(30)
# student2.set_height(180)
# print(student2.name)
#
# print("++++++++++++++++++++")
#
# class People():
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def info(self):
#         print(f"Name is{self.name}\nAge is {self.age}\nHeight is{self.height}")
#
# teacher = People("Vardan",26, 160)
# teacher.info()
# print(teacher.name)