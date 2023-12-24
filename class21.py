# #Inheritance
# class Pen:   # PARENT CLASS   #BASE CLASS  
#     width = 2
#     unit = "cm"
#     height = 15
#     color = ""
#    # Single Inheritance
# class Person(Pen):  # CHILD CLASS #DERIVED CLASS
#     name = ""
#     email = ""
#     age = 0

# p1 = Person()
# print(p1.width)   
# print(p1.age)

# class A:
#     x = 0
#     y = 0
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def sum(self):
#         return self.x + self.y
    


# class B(A):
#     z = 0
#     def __init__(self, x,y):
#         self.z = x
       
#     def getData(self):
#         super().__init__(50, 90)
#         return self.z
    
# b1 = B(30,70)
# d = b1.sum()
# print(d)
# e = b1.getData()
# d = b1.sum()
# print(d)
# print(e)




# class A:
#     x = 7
# class B(A):
#     y = 8
#     def __init__(self):
#         print(super().x)
# class C(B):
#     z = 78

# c1 = C()
# print(c1.x)

# print(c1.y)


class A:
    _a = 90
    x = 30


# class B(A):
#     z = 80
#     def __init__(self):
#         print(self._a)
       

a1 = A()
print(a1._a)



class Student:
    _schoolName = 'XYZ School' # protected class attribute
    
    def __init__(self, name, age):
        self._name=name  # protected instance attribute
        self._age=age # protected instance attribute
s1 = Student("Nishant",34)
s1._schoolName = "hello"
print(Student._schoolName)


# class D:
#     def __gg():

