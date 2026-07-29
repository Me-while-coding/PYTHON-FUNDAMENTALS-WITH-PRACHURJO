
age = int(input("enter your age "))
try:
    if(age < 0):
        raise ValueError("Invalid age!")

except ValueError as e:
    print(e)
else:
    print("age is valid")

ValueError
FileNotFoundError
ZeroDivisionError
ArithmeticError
IndexError
KeyError


