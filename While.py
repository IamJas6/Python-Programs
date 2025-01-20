''' While loop Programs '''
#1. WAP to print first 10 natural numbers along with its cube
# i=1
# while i <= 10:
#     print(i,'cube',i**3)
#     i+=1

#2. WAP to print first 10 natural number in reverse order
# i = 10
# while i >= 1:
#     print(i)
#     i-=1

#3. WAP to print sum of first 10 natural numbers 
# i=1
# s=0
# while i<=10:
#     s+=i
#     print(s)
#     i+=1

#4. WAP to print characters present in the given string
# s=input('enter string: ')
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1

#5. WAP to copy characters present in one string to another string
# s=input('enter string: ')
# st=''
# i=0
# while i<len(s):
#     st+=s[i]
#     i+=1
# print(st)

#6. WAP to copy value present in one list to other list
# l=[1,2,3,4,5]
# li=[]
# i=0
# while i<len(l):
#     li+=[l[i]]
#     i+=1
# print(li)

#7. WAP to print goodmorning exactly 5 times
# i=1
# while i<=5:
#     print('GoodMorning')
#     i+=1

#8. WAP to print all even numbers from range 1 to 50
# i=1
# while i<=50:
#     if i%2==0:
#         print(i)
#     i+=1

#     or
# i=0
# while i<=50:
#     print(i)
#     i+=2

#9. WAP to print all character which is present at even index from given string
# s=input('enter string: ')
# i=0
# while i<len(s):
#     print(s[i])
#     i+=2

#10. WAP to extract all hte lower alphabets present in the given string
# s=input('enter string: ')
# i=0
# while i<len(s):
#     if 'a'<=s[i]<='z':
#         print(s[i],end=' ')
#     i+=1

#11. WAP to extract all the special characters present at odd index from given string
# s=input('enter string: ')
# i=0
# while i<len(s):
#     if not ('a'<=s[i]<='z' or 'A'<=s[i]<='Z' or '0'<=s[i]<='9'):
#         print(s[i],end=' ')
#     i+=1

#12. WAP to print factorial of given integer number
# n=int(input('enter number: '))
# f=1
# i=1
# while i<n:
#     f=f*i
#     i+=1
#     print(f,end=' ')

#13. WAP to check whether the given integer number is palindrome or not
# n=int(input('ener number: '))
# a=n
# p=0
# while n>0:
#     r=n%10
#     p=p*10+r
#     n=n//10
# if p==a:
#     print('number is palindrome')
# else:
#     print('number is not palindrome')

#14. WAP to seperate all different characters present in the given string to different variables
# s=input('enter string: ')
# i=0
# u=''
# l=''
# sp=''
# n=''
# while i<len(s):
#     if 'a'<=s[i]<='z':
#         l+=s[i]
#     elif 'A'<=s[i]<='Z':
#         u+=s[i]
#     elif '0'<=s[i]<='9':
#         n+=s[i]
#     else:
#         sp+=s[i]
#     i+=1
# print(u,l,sp,n)

#15. WAP to check whether the given string is palindrome or not without using slicing
# s=input('enter string: ')
# st=''
# i=0
# while i<len(s):
#     st=s[i]+st
#     i+=1
# if st==s:
#     print('string is palindrome')
# else:
#     print('string is not palindrome')

#16. WAP to toggle the given input string
# s=input('enter string: ')
# i=0
# st=''
# while i<len(s):
#     if 'A'<=s[i]<='Z':
#         st+=chr(ord(s[i])+32)
#     elif 'a'<=s[i]<='z':
#         st+=chr(ord(s[i])-32)
#     else:
#         st+=s[i]
#     i+=1
# print(st)

#17. WAP to print product of individual digits of given integere number
# n=int(input('enter number: '))
# p=1
# while n>0:
#     r=n%10
#     p=p*r
#     n=n//10
# print(p)

#18. WAP to extract all the complex data items present in heterogenous list collection if length of output is >=3
# then print output list else print input list
# l=[3+4j,'a',4+2j,6+3j]
# li=[]
# i=0
# while i<len(l):
#     if type(l[i])==complex:
#         li+=[l[i]]
#     i+=1
# if len(li)>=3:
#     print(li)
# else:
#     print(l)

#19. WAP to find sum of ascii value of all lower case alphabets present at even index from string only if string is odd
# s=0
# st=input('enter string: ')
# i=0
# if len(st)%2==1:
#     while i<len(st):
#         if 'a'<=st[i]<='z':
#             s+=ord(st[i])
#         i+=2
#     print(s)
# else:
#     print('even string')

#20. WAP to priont the following series 10,20,30,...,200.
# i=10
# while i<=200:
#     if i==200:
#         print(i,end='.')
#     else:
#         print(i,end=',')
#     i+=10

#21. WAP to print the following output
#I/P: 'roses are red'
#O/P: ['sesor',3,'der']
# s=input('enter string: ')
# st=s.split()
# i=0
# l=[]
# while i<len(st):
#     if i%2==0:
#         l+=[st[i][::-1]]
#     else:
#         l+=[len(st[i])]
#     i+=1
# print(l)

#22. WAP to get the following output
# I/P: 'i am a fan of vijay'
# O/P: {'i':1, 'am':2, 'a':1, 'fan':3, 'of':2, 'vijay':5}
# s=input('enter string: ')
# d={}
# i=0
# st=s.split()
# while i<len(st):
#     d[st[i]]=len(st[i])
#     i+=1
# print(d)

#23. WAP to get the following 
# I/P: 'i am a fan of vijay'
# O/P: {'i':1, 'am':1, 'a':1, 'fan':1, 'of':1, 'vijay':2}
# s=input('enter string: ')
# st=s.split()
# d={}
# ind=0
# while ind<len(st):
#     for j in st:
#         c=0
#         for i in j:
#             if i in 'aeiouAEIOU':
#                 c+=1
#         d[j]=c
#     ind+=1
# print(d)

#24. WAP to extract all even integers numbers present at odd index from given heterogenous list collection
# l=[1,2,4,6,7,8,9,12,'a','ab']
# i=0
# li=[]
# while i<len(l):
#     if type(l[i])==int and l[i]%2==0 and i%2==1:
#         li+=[l[i]]
#     i+=1
# print(li)

#25. WAP to remove all duplicate values present in the given list collection
# l=[1,2,3,3,4,5,5,6,'a','a','b','b']
# i=0
# li=[]
# while i<len(l):
#     if l[i] not in li:
#         li+=[l[i]]
#     i+=1
# print(li)

#26. WAP to store ascii value of all the lower case alphabets present in the given string only if it is odd
# s=0
# st=input('enter string: ')
# i=0
# while i<len(st):
#     if 'a'<=st[i]<='z' and ord(st[i])%2==1:
#         s+=ord(st[i])
#     i+=1
# print(s)

#27. WAP to check the given integer nuber is prime or not
# n=int(input('enter number: '))
# i=2
# c=0
# while i<n:
#     if n%i==0:
#         c+=1
#     i+=1
# if c==0:
#     print('Prime number')
# else:
#     print('not Prime number')

#28. WAP to check the given integer number is perfect or not
# n=int(input('enter number: '))
# s=0
# i=1
# while i<n:
#     if n%i==0:
#         s+=i
#     i+=1
# if s==n:
#     print('Perfect number')
# else:
#     print('Not Perfect number')

#29. WAP to check the given integer number is armstrong number or not
# n=int(input('enter number: '))
# a=n
# l=len(str(n))
# s=0
# while n>0:
#     r=n%10
#     s+=r**l
#     n=n//10
# if s==a:
#     print('armstrong number')
# else:
#     print('not armstrong number')

#30. WAP to split given heterogenous list to single and multi value collection
# l=[56,7.8,'ab',[8,9],False,{1:2}]
# M=[]
# S=[]
# i=0
# while i<len(l):
#     if type(l[i]) in [int,float,complex,bool]:
#         S+=[l[i]]
#     else:
#         M+=[l[i]]
#     i+=1
# print('Single value data :',S)
# print('Multi Value data: ',M)