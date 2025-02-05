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
# class A:
#     a=10
#     b=20

# class B(A):
#     def __init__(self,c,d):
#         self.c=c
#         self.d=d
# ob = B(30,40)
# print(ob.a,ob.b,ob.c,ob.d)

#Example
# class bank1:
#     bname = 'sbi'
#     branch = 'mysore'
#     def __init__(self, name, acc,phn ):
#         self.name = name
#         self.acc = acc
#         self.phn = phn
#     def display(self):
#         print(self.name,self.acc,self.phn)
#     def ch_name(self,new):
#         self.name = new
#     @classmethod
#     def show(cls):
#         print(cls.bname,cls.branch)
#     @classmethod
#     def ch_bname(cls, new):
#         cls.bname = new

# class bank2(bank1):
#     def __init__(self, name,acc,phn,adhar,pan):
#         bank1.__init__(self,name,acc,phn)
#         self.adhar = adhar
#         self.pan = pan
#     def display(self):
#         super().display()
#         print(self.adhar,self.pan)
# c1 = bank1('suhail',242424,123456789)
# c2 = bank2('saleem',262626,987654321,'adh1234','pan1234')
# c1.display()
# print()
# c1.show()
# print()
# c2.display()

#2. Multilevel Inheritance
# class A:
#     a=20
# class B(A):
#     b = 20
# class C(B):
#     c = 30
# ob = C()
# print(ob.a, ob.b, ob.c)

#Example
# class resume1:
#     qual = '10th'
#     def __init__(self,name,phn,tper):
#         self.name = name
#         self.phn = phn
#         self.tper = tper
#     def display(self):
#         print(self.name)
#         print(self.phn)
#         print(self.tper)
#     @classmethod
#     def show(cls):
#         print(cls.qual)
    
# class resume2(resume1):
#     qual = '12th'
#     def __init__(self, name,phn,tper,twper):
#         resume1.__init__(self,name,phn,tper)
#         self.twper = twper
#     def display(self):
#         super().display()
#         print(self.twper)
#     @classmethod
#     def show(cls):
#         print(cls.qual)
# class resume3(resume2):
#     qual = 'grad'
#     def __init__(self, name,phn,tper,twper,gper):
#         resume2.__init__(self,name,phn,tper,twper)
#         self.gper = gper
#     def display(self):
#         super().display()
#         print(self.gper)
#     @classmethod
#     def show(cls):
#         print(cls.qual)

# r1 = resume1('suhail',1234567890,81.16)
# r2 = resume2('suhail',1234567890,81.16,84.16)
# r3 = resume3('suhail',1234567890,81.16,84.16,87)

# r3.show()
# r3.display()


#3. Multiple Inheritance
# class A:
#     a=10
# class B:
#     b=20
# class C:
#     c=30
# class D(A,B,C):
#     pass

# ob = D()
# print(ob.a, ob.b, ob.c, ob.d)

#Example
# class add:
#     @staticmethod
#     def add(a,b):
#         return a+b
# class sub:
#     def sub(a,b):
#         return a-b
# class mul:
#     def mul(a,b):
#         return a*b
# class result(add,sub,mul):
#     pass
# print(result.add(10,5))
# print(result.sub(10,5))
# print(result.mul(10,5))

#4. Hierarchical inheritance
# class A:
#     a=10
# class B(A):
#     pass
# class C(A):
#     pass

# print(B.a)
# print(C.a)

#Example
# class tyss:
#     iname = ''
#     def __init__(self,name,phn):
#         self.name = name
#         self.phn = phn
#     def display(self):
#         print(self.name,self.phn)
#     @classmethod
#     def show(cls):
#         print(cls.iname)
# class Q(tyss):
#     iname = 'Qspiders'
# class P(tyss):
#     iname = 'Pyspiders'

# tyss.show()
# Q.show()
# P.show()