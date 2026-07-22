# head A:
#     head B:
#       head C :
#         head D :


#jo log 55 ko upar hain woh senior citizen hain, jo log 55 se neeche hain lekin
#30 min age hain fir they are adults, agar 18 to 30 age -> young adult and < 18: not adult

# age = int(input("Enter your age : "))
# if(age < 120 and age > 0):
#     if(age >= 55) :
#         print("you are a senior citizen")
#     elif(age >=30) :
#         print("you are an adult")
#     elif(age >= 18) :
#         print("you are a young adult")
#     else :
#         print("Tum kuch bhi nhi ho")
# else : 
#     print("Enter a valid age!")

choice = int(input("Enter your choice : "))

match choice:
    case x if x > 0:
        print("you have entered positive")
    case x if x < 0:
        print("you have entered negative")
    case _ : 
        print("you have entered 0")
