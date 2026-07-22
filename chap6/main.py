# a = input("enter your input")

# for i  in range(20,1,-1):
#     print(i)


# range(n) -> integral numbers from 0 to n-1, including extreme sides

# range(start,stop,step)

#while : jab tak condition true hain tab tak chalte jao

# a = 20
# while(a > 0):
#     print(a)
#     a -=1

# for i in range(1,11):
#     if(i > 5):
#         break
#     print(i)

# for i in range(2,11):
#     if(i%2 == 1):
#         continue
#     print(i)
#     print("Hello")


# for i in range(2,11):
#     if(i%2!=0):
#         pass
#     print(i)
#     print("Hello")


n = int(input("Enter number of lines : "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end = " ")
#     print("")


# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end= " ")
#     print();


# for i in range(1,n+1):
#     for gaps in range(n-i):
#         print(" ",end="")
#     for stars in range(2*i-1):
#         print("*",end="")
#     print("")

for i in range(1,21):
    print(i)
    if(i==10):
        break
else :
    print("I have executed all steps successfully")