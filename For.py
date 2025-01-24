#1. WAP to extract all the integer present inside heterogenous list
# l=[2,3,4j,True]
# li=[]
# for i in l:
#     if type(i)==int:
#         li+=[i]
# print(li)

#2. WAP to extract all integer numbers which is more than 15 from given heterogeneous list
# l=[5,'a',15,18,6j]
# li=[]
# for i in l:
#     if type(i)==int and i>15:
#         li+=[i]
# print(li)

#3. WAP to remove all duplicate characters present in string
# s=input('enter string: ')
# st=''
# for i in s:
#     if i not in st:
#         st+=i
# print(st)

#4. WAP to count number of upper alphabet present in string
# s=input('enter string: ')
# c=0
# for i in s:
#     if 'A'<=i<='Z':
#         c+=1
# print(c)

#5. WAP to split given string into substring without split function
# s=input('enter string: ')
# st=['']
# for i in s:
#     if i == ' ':
#         st+=['']
#     else:
#         st[-1]+=i
# print(st)

#6. WAP to spit the string based on specified character and specified number of times
# s=input('enter string: ')
# c=input('enter character: ')
# n=int(input('enter number: '))
# st=['']
# for i in s:
#     if i == c and len(st)<=n:
#         st+=['']
#     else:
#         st[-1]+=i
# print(st)

#7. WAP to reverse given string without slicing
# s=input('enter string: ')
# st=''
# for i in s:
#     st=i+st
# print(st)

#8. WAP to print all characters present at the even index from string using for loop
# s=input('enter string: ')
# st=''
# for i in range(0,len(s),2):
#     st+=s[i]
# print(st)

#9. WAP to extract all string data items whose length is >= 3 and present at odd index from heterogeneous list
# l=['abc','cda',6,7j,'bca']
# li=[]
# for i in range(1,len(l),2):
#     if type(l[i])==str:
#         li+=[l[i]]
# print(li)

#10. WAP check intefer number is perfect or not
# n=int(input('enter number: '))
# s=0
# for i in range(1,n):
#     if n%i==0:
#         s=s+i
# if s==n:
#     print('perfect number')
# else:
#     print('not perfect number')

#11. WAP to check the given integer number is armstrong number or not
# n=int(input('enter number: '))
# s=0
# st=str(n)
# l=len(st)
# for i in st:
#     s+=int(i)**l
# if s==n:
#     print('armstrong number')
# else:
#     print('not armstrong number')

#12. WAP to create the dictionary where key should be of only string datatype
# d={'a':5,'b':6,5:55}
# di={}
# for i in d:
#     if type(i)==str:
#         di[i]=d[i]
# print(di)

#13. WAP to print initial index position of a character present inside string
# s=input('enter string: ')
# c=input('enter char: ')
# for i in range(len(s)):
#     if s[i]==c:
#         print(i,s[i])
#         break

#14. WAP to print small divisor of given integer number except 1
# n=int(input('enter number: '))
# for i in range(2,n):
#     if n%i==0:
#         print(i)
#         break


#15. WAP to check whether the given integer number is prime or not
# n=int(input('enter number: '))
# for i in range(2,n):
#     if n%i==0:
#         print('not prime')
#         break
# else:
#     print('prime')

#16. WAP to check whether user is entering correct email id or not if it is not correct then ask user to enter the correct email id 
#continously if it is correct stop the loop
# email='example@example.com'
# while True:
#     e=input('enter email: ')
#     if e==email:
#         print('Same')
#         break
#     else:
#         print('re type')

#17. WAP to guess number
# N=69
# while True:
#     n=int(input('enter number: '))
#     if N==n:
#         print("Hurray!!")
#         break
#     else:
#         print("OOoops Wrong")

#18. WAP to print only even numbers from range 1 to 50 by using continue statement
# for i in range(1,51):
#     if i%2==0:
#         print(i)
#     else:
#         continue

#19. WAP to print given output using nested for loop
#I/P: 'India is the best country'
#O/P: {'India':5,'is':2,'the':3,'best':4,'country':7}
# s=input('enter string: ')
# d={}
# st=s.split()
# for i in st:
#     c=0
#     for j in i:
#         c+=1
#     d[i]=c
# print(d)


#20. WAP to get the following output
#I/P: 'we are the best'
#O/P: [('we',2),('are',3),('the',3),('best',4)]
# s=input('enter string: ')
# st=s.split()
# l=[]
# for i in st:
#     c=0
#     for j in i:
#         c+=1
#     l+=[(i,c)]
# print(l)

#21. WAP to get the following output
#I/P: 'we are the best'
#O/P: {'we':1,'are':2,'the':1,'best':1}
# s=input('enter string: ')
# st=s.split()
# d={}
# for i in st:
#     c=0
#     for j in i:
#         if j in 'aeiouAEIOU':
#             c+=1
#     d[i]=c
# print(d)

#22. WAP to get the following output
#I/P: 'aaabbabcad'
#O/P: {'a':5,'b':3,'c':1,'d':1}
# s=input('enter string: ')
# d={}
# for i in s:
#     c=0
#     for j in s:
#         if j==i:
#             c+=1
#     d[i]=c
# print(d)

#23. WAP to get the following output
#I/P: 'aaabbabcacd'
#O/P: 'a5b3c2d1'
# s=input('enter string: ')
# st=''
# for i in s:
#     if i not in st:
#         c=0
#         for j in s:
#             if j==i:
#                 c+=1
#         st+=i+str(c)
# print(st)
