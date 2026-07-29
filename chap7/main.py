
# # print("""This is a multiline
# # string written with triple
# #  quotes""")

# # s = "ABCDEF"
# # print(s[1:4])
# # print(s[:3])
# # print(s[3:])
# # print(s[::-1])

# # print(s[1:4]) # ending index hain who exclusive hota hain / count nhi hota
# # print(s)

# # print(s[::-1])

# # del s
# # print(s)

# # s1 = s.replace("AB","123")
# # print(s1)

# # print("I want to print " * 10)

# # a = "           this is a sentence#!###!!!##!!!                    "
# # print(a.strip("!# "))

# # name = "Sagnik"
# # marks = 100
# # print("{} has scored {} in maths".format(name,marks))

# # print("s" in "geeks for geeks")

# # laptop_spcs = ['Asus TUF A15',360.56,16,512,3050,True]

# # for i in laptop_spcs:
# #     print(i)

# # list_of_ones = [1] * 10
# # print(list_of_ones)

# # laptop_spcs[2] = 32
# # print(laptop_spcs)

# # l = [1,2,3]
# # # l.append(4)
# # print(l)
# # l.append([4,5])
# # print(l)

# l.extend("Prachurjo")
# # print(l)

# l.insert(0,"first")
# # print(l)

# l.remove('r')
# # print(l)

# l.pop()
# print(l)
# l.pop()
# print(l)

# del l[2:]
# print(l)

# l.clear()
# print(l)

# tup = (1,2,3,4,5,6)

# a,b,*c,d = tup
# print(a,b,c,d)

#union
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1 = s1 | s2
# print(s1)

#intersection
# s1 = s1 & s2
# print(s1)

#difference
# s1 = s1-s2 # all elements of s1 which are not in s2

#sym_diff : elements present in either of the sets but not in both
# # s1 ^ s2

student1 = {"name":"Zishan",
            "age" : 18,
            "grade" : 9,
            "percent":98.5}

# print(student1["age"])
# print(student1["address"])
# print(student1.get("address","address not registered"))

student1["address"] = "park street,house no. 3,opposite to Rajni sweet shop,Jalandhar,Punjab"
# print(student1)

student1.update({"email" : "abc@gmail.com","team":"red"})
# print(student1)

#duplicate keys nhi ho sakte dict mein

student2 = {"name":"Vansh",
            "name":"Prabal",
            "cgpa":9.6}
# print(student2)

# keys must be immutable : strings , tuples , numbers
# values can be mutable : list , sets , dictionary


students = {
    101 : {"name":"yash",
           "marks": 89},
    102 : {"name" : "prabal",
           "marks" : 85},
    103 : {"name" : "Ishu",
           "marks" : 100}
}

# print(students[102]["marks"])

# # del students[101]
# # print(students)

# a = students.pop(102)
# print(students)
# print(a)


# class_strength = {6:100,7:100}
# print(class_strength)


# for i in students.keys():
#     print(i)

# for i in students.values():
#     print(i)

# for key,val in students.items():
#     print(f"key = {key} , value = {val}")

l1 = ["apples","pineapples","mangoes"]
# l2 = [10,5,9]
# l3 = set(zip(l1,l2))
# print(l3)


# fruits = dict.fromkeys(l1,10)
# print(fruits)

# n = int(input("enter a limit : "))
# first_n_pow_of_2 = [2**i for i in range(1,n+1)]

# print(first_n_pow_of_2)

 
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# sum = [(x,y,z) for x in l for y in l for z in l if (x+y+z == 24 and (x!=y and y!=z and z!=x) and (x<z)) ]

# print(sum)

name = "Prachurjo"

# d = {k:ord(k) for k in name}
# print(d)

d = {i:i**2 for i in l}
print(d)