#Generic States
# class A:
#     a=10
#     b=20
# ob = A()

# print(A.a,A.b)
# print(ob.a,ob.b)

# print("After class variable modifications")
# A.a=30
# print(A.a,A.b)
# print(ob.a,ob.b)

# print("After object variable modifications")
# ob.a=40
# print(A.a,A.b)
# print(ob.a,ob.b)

# print("After 2nd class variable modifications")
# A.a=50
# print(A.a,A.b)
# print(ob.a,ob.b)

#Specific states
# class A:
#     a=10
#     b=20
#     def __init__(self,c,d):
#         self.c = c
#         self.d = d
# ob = A(30,40)
# print(A.a,A.b)
# print(ob.a,ob.b,ob.c,ob.d)

# class A:
#     def __init__(self,name,sid):
#         self.name = name
#         self.sid = sid

# ob = A('suhail',403)
# print(ob.name, ob.sid)

# 3 -> types of methods
# 1. Object method
# class school:
#     teacher = 'Rida'
#     sub = 'Python'
#     branch = 'cs'

#     def __init__(self, sname,sid,roll,per,sub,branch):
#         self.sname = sname
#         self.sid = sid
#         self.roll = roll
#         self.per = per
#         self.sub = sub
#         self.branch = branch
    
#     def display(self):
#         print(f"Student Name: {self.sname}")
#         print(f"Student ID: {self.sid}")
#         print(f"Roll Number: {self.roll}")
#         print(f"Percentage: {self.per}")
#         print(f"Subject: {self.sub}")
#         print(f"Branch: {self.branch}")

#     def ch_name(self,new):
#         self.sname = new

#     def ch_sid(self,new):
#         self.sid = new

#     def ch_roll(self,new):
#         self.roll = new

#     def ch_per(self,new):
#         self.per = new
    
#     def ch_sub(self,new):
#         self.sub = new
    
#     def ch_branch(self,new):
#         self.branch = new

# s1 = school('suhail',1,403,90,'python','cs')
# s2 = school('yasir',2,404,80,'ML','ECE')

# s1.display()
# print()
# s2.display()
# print()

# s1.ch_name('Rahul')
# s1.ch_sid(2)
# s1.ch_roll(405)
# s1.ch_per(85)
# s1.ch_sub('DSA')
# s1.ch_branch('IT')

# s1.display()

#2. Class Method
