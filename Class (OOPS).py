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

#Encapsulation
#operator overloading / magic methods

#1. bitwise operations
# class bit:
#     def __init__(self, num):
#         self.num = num
#     def __lshift__(self,other):
#         return self.num<<other.num
#     def __rshift__(self,other):
#         return self.num>>other.num
#     def __and__(self, other):
#         return self.num&other.num
#     def __or__(self, other):
#         return self.num|other.num
#     def __xor__(self, other):
#         return self.num^other.num

# ob1 =bit(2)
# ob2 = bit(3)
# print(ob1<<ob2)
# print(ob1>>ob2)
# print(ob1&ob2)
# print(ob1|ob2)
# print(ob1^ob2)

#2. Relational operator
# class rel:
#     def __init__(self,num):
#         self.num = num
#     def __lt__(self,other):
#         return self.num<other.num
#     def __gt__(self,other):
#         return self.num>other.num
#     def __le__(self,other):
#         return self.num<=other.num
#     def __ge__(self,other):
#         return self.num>=other.num

# ob1 = rel(10)
# ob2 = rel(15)
# print(ob1<ob2)
# print(ob1>ob2)
# print(ob1<=ob2)
# print(ob1>=ob2)

#1. WAP to create a class for a library and demonstrate single level inheritance with contructor & method chaining
# class library:
#     def __init__(self, lname,branch):
#         self.lname = lname
#         self.branch = branch
#     def display(self):
#         print("Library Name: ", self.lname)
#         print("Branch: ", self.branch)
# class member(library):
#     def __init__(self, lname,branch,mname,mid):
#         library.__init__(self, lname,branch)
#         self.mname = mname
#         self.mid = mid
#     def display(self):
#         super().display()
#         print("Member Name: ", self.mname)
#         print("Member ID: ", self.mid)

# l1 = library('Philos', 'Mysore')
# l2 = library('Philos', 'Banglore')
# m1 = member('Philos', 'Mysore','Suhail','S1')
# m2 = member('Philos', 'Banglore','Yasir','Y1')

# print('Libraries')
# l1.display()
# print()
# l2.display()
# print()

# print('Details')
# m1.display()
# print()
# m2.display()

#2. WAP to create a class for vehicle and demonstrate multilevel inheritance
# class vehicle:
#     def __init__(self, vname, vtype):
#         self.vname = vname
#         self.vtype = vtype
#     def display(self):
#         print("Vehicle Name: ", self.vname)
#         print("Vehicle Type: ", self.vtype)

# class details(vehicle):
#     def __init__(self, vname, vtype, price):
#         vehicle.__init__(self, vname, vtype)
#         self.price = price
#     def display(self):
#         super().display()
#         print("Price: ", self.price)
# class member(details):
#     def __init__(self, vname, vtype, price, mname, mid):
#         details.__init__(self, vname, vtype, price)
#         self.mname = mname
#         self.mid = mid
#     def display(self):
#         super().display()
#         print("Member Name: ", self.mname)
#         print("Member ID: ", self.mid)

# v1 = vehicle('BMW M5 CS', 'Sedan')
# v2 = vehicle('Polo GT', 'Sedan')

# d1 = details('BMW M5 CS', 'Sedan', '2,50,00,000')
# d2 = details('Polo GT', 'Sedan', '8,00,000')

# m1 = member('BMW M5 CS', 'Sedan', '2,50,00,000','Suhail','S1')
# m2 = member('Polo GT', 'Sedan', '8,00,000','Yasir','Y1')

# print('Vehicles',end="\n")
# v1.display()
# print()
# v2.display()
# print()

# print('Details',end="\n")
# d1.display()
# print()
# d2.display()
# print()

# print('Members',end="\n")
# m1.display()
# print()
# m2.display()


#3. WAP to create a class for travel agency and show multiple inheritance with chaining
# class flightbook:
#     def __init__(self, place, tprice):
#         self.place = place
#         self.tprice = tprice
#     def display(self):
#         print("Place: ", self.place)
#         print("Ticket Price: ", self.tprice)
# class hotelbook:
#     def __init__(self, hname, rprice):
#         self.hname = hname
#         self.rprice = rprice
#     def show(self):
#         print("Hotel Name: ", self.hname)
#         print("Room Price: ", self.rprice)

# class travelagency(flightbook, hotelbook):
#     def __init__(self, place,tprice,hname,rprice,tname,branch):
#         flightbook.__init__(self, place, tprice)
#         hotelbook.__init__(self, hname, rprice)
#         self.tname = tname
#         self.branch = branch
#     def display(self):
#         super().display()
#         super().show()
#         print("Travel Agency Name: ", self.tname)
#         print("Branch: ", self.branch)

# f1 = flightbook('Tokyo', '1,50,000')

# h1 = hotelbook('Tokyo Hotel', '25,000')

# T1 = travelagency('Tokyo', '1,50,000', 'Tokyo  Hotel', '25,000', 'Mysore Travels', 'Mysore')

# print('Flight Detail', end='\n')
# f1.display()
# print()

# print('Hotel Details', end='\n')
# h1.show()
# print()

# print('Travel Detail', end='\n')
# T1.display()


#4. WAP to create a class for hospital and perform hierarchical inheritance
# class hospital:
#     def __init__(self, hname, phn):
#         self.hname = hname
#         self.phn = phn
#     def display(self):
#         print("Hospital Name: ", self.hname)
#         print("Phone Number: ", self.phn)
# class doctor(hospital):
#     def __init__(self, hname, phn, dname, specialization):
#         hospital.__init__(self, hname, phn)
#         self.dname = dname
#         self.specialization = specialization
#     def display(self):
#         super().display()
#         print("Doctor Name: ", self.dname)
#         print("Specialization: ", self.specialization)
# class patient(hospital):
#     def __init__(self, hname, phn, pname, age):
#         hospital.__init__(self, hname, phn)
#         self.pname = pname
#         self.age = age
#     def display(self):
#         super().display()
#         print("Patient Name: ", self.pname)
#         print("Age: ", self.age)

# h1 = hospital('Manipal Hospital', '1234567890')

# d1 = doctor('Manipal Hospital', '1234567890', 'Dr. Alok', 'Cardiologist')

# p1 = patient('Manipal Hospital', '1234567890', 'John Doe', 35)

# print('Hospital Detail', end='\n')
# h1.display()
# print()

# print('Doctor Detail', end='\n')
# d1.display()
# print()

# print('Patient Detail', end='\n')
# p1.display()