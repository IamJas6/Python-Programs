#Built in iterators
#1. iter()
#2. next()

#Example
# l=[1,2,3,4]
# inital_value = iter(l)
# print(next(inital_value))
# print(next(inital_value))
# print(next(inital_value))
# print(next(inital_value))
# # print(next(inital_value))  //stop iteration error

#User defined iterators
#1. __iter__() method
#2. __next__() method

#Example
#1. WAP to print first n natural numbers
# class nat:
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):
#         self.i = 1
#         return self
#     def __next__(self):
#         if self.i <= self.n:
#             res = self.i
#             self.i+=1
#             return res
#         else:
#             raise StopIteration
# ob = nat(int(input('enter number: ')))
# print(list(ob))

#2. WAP to create a user defined range function by using user defined iterators
# class range:
#     def __init__(self,s,e,u=1):
#         self.s=s
#         self.e=e
#         self.u=u
#     def __iter__(self):
#         self.i = self.s
#         return self
#     def __next__(self):
#         if self.i < self.e:
#             res = self.i
#             self.i += self.u
#             return res
#         else:
#             raise StopIteration

# r = range(0,7,2)
# print(list(r))

#3. WAP to print squarre of all even numbers from range one to ten else print the cube if numbers
# class sq:
#     def __init__(self,s,e,u=1):
#         self.s=s
#         self.e=e
#         self.u=u
#     def __iter__(self):
#         self.i=self.s
#         return self
#     def __next__(self):
#         if self.i<self.e:
#             if self.i%2==0:
#                 res = self.i**2
#             else:
#                 res = self.i**3
#             self.i+=self.u
#             return res
#         else:
#             raise StopIteration

# r = sq(0,7)
# print(list(r))