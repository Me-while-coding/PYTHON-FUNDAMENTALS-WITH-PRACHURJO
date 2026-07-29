# import mod as m

# m.add(1,2)

# m.isEven(3453)

# print(m.ultimate_weapon * 34)


# import math
# print(math.sqrt(34))


# res = lambda x: x%3 == 0 and x%5 == 0
# for i in range(1,5):
#     print(res(i))

# l = [1,2,3,4,5]
# n = int(input())
# l1 = list(map(lambda x:x+n,l))

# print(l1)

# s = 'abracadabra'
# S = list(map(lambda x:x.upper(),s))

# print(S)

# l = [ 3 , 5 ,15 , 30 , 24 ,33, 45 , 44, 21, 75 , 90 , 43,25 ,66 ,72]

# l1 = list(filter(lambda x:x%3==0 and x%5==0,l))
# print(l1)

from functools import reduce

l = [4,5,6,7,9,10,11]
prod = reduce(lambda x,y:x+y, l)
print(prod)