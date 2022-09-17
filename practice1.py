# # 1st
# # a = 'length of a number'
# # print(len(a))
# # 2nd
# # b = '3'
# # print(type(b))
# # c = int(b)
# # print(c)
# # print(type(c))
# # x = '3.5'
# # print(type(x))
# # y = float(x)
# # print(type(y))
# # 3rd
# # a = [('hemanth', 24), ('kumar', 22)]
# # print(type(a))
# # b = dict(a)
# # print(b)
# # print(type(b))
# # 4th
# # a = ['hemanth', 'kumar', 33, 22.8]
# # b = tuple(a)
# # print(b)
# # print(type(b))
# # print(type(a))
# # c = list(b)
# # print(type(c))
# # 5th
# # a = {'hemanth':24, 'kumar':22, 'manikonda':1998}
# # print(type(a))
# # a.update(hemanth=22,kumar = 24, manikonda = 1999, anjibabu = 22)
# # print(a)
# # 6th
# # a = [2, 34, 2, 2, 2, 34, 22, 34.9, 'hemanth']
# # b = ('hemanth', 'kumar', 55, 'ku')
# # print(a.count(2))
# # print(a.index('hemanth'))
# # print(a.remove(34))
# # print(a.pop())
# # 7th
# # input = 'welcome to python'
# # a = input()
# # print(a[::-1])
# # 8th
# # a = 'hemanth'
# # print(a[::-1])
# # 9th
# # a = [10, 5, 4, 20, 1, 15, 12]
# # a.sort()
# # print(a)
# # 10
# # a = [i for i in list if ]
#
# # print([x**2 for x in range(10,20) if x%2 == 0])
# # print([i for i in range(10) if i%2 != 0])#output will be in odd numbers
# # print([i for i in range(10) if i%2 == 0])#output will be in even numbers
# # h1 = [1,2,3,4,5,65,6,6]
# # print({i for i in h1 if i %2 != 0})
# # print({i : i*i for i in h1 }
# # print(list(range(1,19)))
# # for i in range(10,1,1):
# #     print(i)
# # l = [11,12,13,14,15,16]
# # for i in range(len(l)):#index base loop concept and its a even or odd type
# #     if i%2 == 0:
# #         print(l[i])
# age = int(input('enter age'))
# # if age > 18 :
# #     print('yes')
# if age <= 18:
#     print('age is 18')
# if age >=18 & age <= 18:
#     print('not accepted')
# else:
#     print('no')
# # print(True+True)
# d = {
#      1:['a','G','K','I'],
#      2:['G','b','c'],
#      3:['a','K','G','c']
#     }
# for i in d:-
#     d.
# print(i)

# l = [1,2,3,4,5]
# for i in range(len(l)):
#     if l[i] == 5:
#         print(i)

# l = [1,2,3,4,5,6,7,8]
# print(l[1])
# [1,0,0,0,5,0,7,0]
# for i in l:
#    if  i % 2 != 0 and i % 3 != 0:
#        print(i)
#    if i % 2 == 0 or i % 3 == 0:
#        print(0)
#        print(i, end = ' ')
# print(','.join(l))
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Child class
#
#
# class Labrador(Dog):
#     def __init__(self, name, age, playfulness):
#         super().__init__(name, age)
#         self.playfulness = playfulness
# Child class
#
#
# class Poodle(Dog):
#     def __init__(self, name, age, potty_trained):
#         super().__init__(name, age)
#         self.potty_trained = potty_trained
# Grandchild class
#
#
# class Labradoodle(Labrador, Poodle):
#     def __init__(self, name, age, playfulness, potty_trained):
#         super().__init__(name, age, playfulness, potty_trained)
#
#
# dogo2 = Labradoodle("Dookie", 2, 'Very playful', 'Yes')
#
# print(dogo2.playfulness, dogo2.potty_trained)
a = [1,2,3,4,5,6,7,8]
a = [k if k%2 != 0 and k%3 != 0 else 0 for k in a]
print(a)