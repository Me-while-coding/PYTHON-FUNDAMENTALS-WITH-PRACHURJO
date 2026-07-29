# name = "Prachurjo"
# branch = "CSE"
# year = 2
# cgpa = 9.29
# sub = ['OOPS','C++','DSA']
# roll_no = 12501011
# mentor = "Dr. Akash"

# class Students:
#     pass


# student1 = Students()
# student2 = Students()
# student3 = Students()

# student1.name = "Prachurjo"
# # print(student1.name)
# student1.age = 21
# # print(student1.age)


# student2.name = "Yash"

# print(student1.name , student2.name)

# print(student2.age)

# print(id(student1))
# print(id(student2))
# print(id(student3))

# class Bank:
#     def __init__ (self,name,bankAcc,email,address = "Address not assigned"):
#         self.name = name
#         self.bankAcc = bankAcc
#         self.email = email
#         self.address = address
#         print("details have been added for",self.name)

#     def display(self):
#         print(f"name = {self.name}")
#         print(f"bankAcc = {self.bankAcc}")
#         print(f"address = {self.address}")
#         print(f"email = {self.email}")

# customer1 = Bank("Prachurjo","4359013213","pc@gmail.com")
# # print(customer1.email)

# customer2 = Bank("Ravi","2432434324","ravi4343@gmail.com","address 1")
# # print(customer2.address)


# customer1.display() # this is equivalent customer1.display(customer1)


# class Students:
#     def __init__ (self,name,roll,age,cgpa):
#         self.name = name
#         self.roll = roll
#         self.age  = age
#         self.__cgpa = cgpa
#     def update_cgpa(self,cgpa):
#         if cgpa > 0 and cgpa <=10:
#             self.__cgpa = cgpa
#             print("cgpa updated")
#         else:
#             print("not a valid cgpa")

# s1 = Students("Prakhar",12501232,21,8.89)
# s1.update_cgpa(10.7)
# print(s1.__dict__)

class bankAcc:
    def __init__(self,balance):
        self.__balance = balance

    def withdraw(self,amt):
        if amt <= self.__balance and amt > 0:
            self.__balance -= amt
            print(f"{amt} has been withdrawn , current balance = {self.__balance}")   
        else:
            print("enter valid amt")
    def deposit(self,amt):
        if amt > 0 :
            self.__balance += amt
            print(f"new balance = {self.__balance} after amt deposited : {amt}")
        else:
            print("invalid amt")
    def balance(self):
        print(self.__balance)


acc = bankAcc(1000)
acc.withdraw(400)
acc.deposit(2000)
acc.balance()
print(acc.__balance)







