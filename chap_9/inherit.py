class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age


    def introduce(self):
        print(f"my name is {self.name} and my age is {self.age}")



class Student(Person):
    def __init__ (self,name,age,grade,marks):
        super().__init__(name,age)
        self.grade = grade
        self.marks = marks

    def introduce(self):
            super().introduce()
            print("I am a student")

s1 = Student("Debdatta",16,9,90)
s1.introduce() # method overriding








# class Teacher:
#      def __init__ (self,name,age,sub,salary):
#           self.name = name
#           self.age = age
#           self.salary = salary
#           self.sub = sub

#      def introduce(self):
#                 print(f"my name is {self.name}")