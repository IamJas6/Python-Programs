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
# class bank:
#     bname = 'sbi'
#     branch = 'mysore'
#     loan = 'True'

#     def __init__(self,cname, acc, phn, branch):
#         self.cname = cname
#         self.acc = acc
#         self.phn = phn
#         self.branch = branch

#     def show(self):
#         print(self.cname)
#         print(self.acc)
#         print(self.phn)
#         print(self.branch)
#         print()
    
#     def ch_cname(self,new):
#         self.cname = new
    
#     def ch_acc(self,new):
#         self.acc = new

#     def ch_branch(self,new):
#         self.branch = new

#     @classmethod
#     def display(cls):
#         print(cls.bname)
#         print(cls.branch)
#         print(cls.loan)
#         print()
    
#     @classmethod
#     def ch_bname(cls,new):
#         cls.bname = new
    
#     @classmethod
#     def ch_branch(cls,new):
#         cls.branch = new

#     @classmethod
#     def ch_loan(cls,new):
#         cls.loan = new

# b1 = bank('suhail',242424,123456789,'mysore')
# b2 = bank('saleem',262626,987654321,'bangalore')

# b1.show()
# b2.show()
# bank.display()

# bank.ch_loan('False')
# bank.ch_bname('HDFC')
# bank.display()


#3 . Static method
# class bank:
#     bname = 'sbi'
#     branch = 'mysore'

#     def __init__(self,cname, acc, phn, bln):
#         self.cname = cname
#         self.acc = acc
#         self.phn = phn
#         self.bln = bln

#     def balance(self, amt):
#         self.bln = self.add(self.bln, amt)
#         self.msg()
    
#     def withdraw(self, amt):
#         if amt<=self.bln:
#             self.bln = self.sub(self.bln,amt)
#             self.msg()
#         else:
#             print('Insufficient balance')
        
#     def show(self):
#         print(self.cname)
#         print(self.acc)
#         print(self.phn)
#         print(self.bln)
#         print()
        
#     @classmethod
#     def display(cls):
#         print(cls.bname)
#         print(cls.branch)
#         print()

#     @classmethod
#     def ch_bname(cls, new):
#         cls.bname = new

#     @staticmethod
#     def msg():
#         print('Transaction successful')

#     @staticmethod
#     def add(a,b):
#         return a+b
    
#     @staticmethod
#     def sub(a,b):
#         return a-b

# b1 = bank('suhail',242424,123456789,1000)
# b2 = bank('saleem',262626,987654321,1500)

# b1.show()
# b2.show()
# bank.display()

# b1.balance(1000)
# b1.show()
# b1.withdraw(500)
# b1.show()


#Single Inheritance