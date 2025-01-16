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