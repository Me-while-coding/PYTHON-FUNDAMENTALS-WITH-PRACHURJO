# l = [23,32,113,320,44,564,123,27,221,500,678,76,45,212]

# def checksumofdigits(i,val):
#     sum=0
#     while(i>0):
#             sum+= i%10
#             i//=10
#     if(sum == val):
#          return 1
#     return 0

# for i in l:
#     a = i
#     if checksumofdigits(i,6) == 1: #ye wala jo line hain that evalutes to true

#         print(a)


def info(name,age,city):
    print(f"name = {name},age = {age}, city = {city}")


# info(name = "Prachurjo",city = "Alipurduar",age = 21)

# def abc(a,b,**c):
#     # print(a,b,c)


# abc(a = 1,b = 2,f = 5, d = 4 , e = 6)


# def coordinates(x,y=0):
#     print(x,y)

# coordinates(10,45)

# def fact(n):
#     # p = 1
#     # for i in range(2,n+1):
#     #     p*=i
#     # return p
#     if n < 2:
#         return 1
#     else:
#         return n * fact(n-1)

# n = int(input("Enter the number u want factorial of : "))
# print(fact(n))


n = int(input("Enter no. of terms in fibonacci series : "))
def fib(i):
    if i == 0 or i == 1:
        return i
    else:
        return fib(i-1) + fib(i-2)
for i in range(n):
    print(fib(i),end = " ")







