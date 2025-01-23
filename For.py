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

