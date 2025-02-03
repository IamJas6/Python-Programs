#1. WAP to check whether atm pin entered by user is correct or not
# def atm():
#     p=1234
#     while True:
#         up=int(input('enter pin: '))
#         if p==up:
#             print('Matched')
#             break
#         else:
#             print('Not Matched, Re-enter pin')
# atm()

#2. WAP to check whether the integer number is perfect or not
# def perfect(n):
#     s=0
#     for i in range(1,n):
#         if n%i==0:
#             s+=i
#     if s==n:
#         return 'Perfect number'
#     else:
#         return 'Not perfect number'
# print(perfect(int(input('enter number: '))))

#3. WAP to extract all the odd numbers from string only if ascii value of that number is odd
# def odd_ascii(s):
#     n=''
#     for i in s:
#         if '0'<=i<='9' and ord(i)%2==1 and int(i)%2==1:
#             n+=i
#     return n
# print(odd_ascii(input('enter string: ')))

#4. WAP get the following
#I/P: '(((78@B)(((())xqrXz5(()()'
#O/P: 5

#I/P: 'xnQr!((5712((((())()(()pnm((()('
#O/P: 9

# def brackets(s):
#     o=0
#     c=0
#     for i in s:
#         if i == '(':
#             o+=1
#         elif i == ')':
#             c+=1
#     return o-c
# print(brackets(input('enter string: ')))

#7. WAP to extract all substrings from given string only if it is having atleast one vowel in it
# def vowel(s):
#     st=s.split()
#     l=[]
#     for i in st:
#         for j in i:
#             if j in 'aeiouAEIOU':
#                 l+=[i]
#                 break
#     return l
# print(vowel(input('enter string: ')))

#8. WAP to get the following 
#I/P: [12,'python','abcd',7.8,'123']
#O/P: [('python',6),('abcd',4),('123',3)]
# def demo(l):
#     li=[]
#     for i in l:
#         if type(i)==str:
#             li+=[(i,len(i))]
#     return li
# print(demo([12,'python','abcd',7.8,'123']))

#9. WAP to extract all integer numbers which are odd from heterogeneous list using recursion function
# def odd_num(l,li=[],i=0):
#     if i>=len(l):
#         return li
#     if type(l[i])==int and l[i]%2==1:
#         li+=[l[i]]
#     return odd_num(l,li,i+1)
# print(odd_num([12,5,3,4]))

#10. WAP to extract all numbers present in string only if it is divisible by 5 using recursion
# def str_num(s,st=[],i=0):
#     if i>=len(s):
#         return st
#     if '0'<=s[i]<='9' and int(s[i])%5==0:
#         st+=[s[i]]
#     return str_num(s,st,i+1)
# print(str_num(input('enter string: ')))

#11. WAP to count number of occurances of special characters present in the string using recursion
# def spl(s,c=0,i=0):
#     if i>=len(s):
#         return c
#     if not ('A'<=s[i]<='Z' or 'a'<=s[i]<='z' or '0'<=s[i]<='9'):
#         c+=1
#     return spl(s,c,i+1)
# print(spl(input('enter string: ')))

#12. WAP to find sum of individual digits of given integer numbers using recursion
# def digit_sum(n,s=0,i=0):
#     if i>=len(str(n)):
#         return s
#     s+=int(str(n)[i])
#     return digit_sum(n,s,i+1)
# print(digit_sum(int(input('enter number: '))))

#13. WAP to extract all complex data present in heterogenous list using yield
# def comp(d):
#     for i in d:
#         if type(i)==complex:
#             yield i
# print(list(comp([2,3,4j,6+5j])))

#14. WAP to generate squares of all numbers based on the value which is specified for n by use. Only if the 
# n is even else generate qubes of the numbers from 1 to n by using the yield
# def gen(n):
#     if n%2==0:
#         for i in range(n+1):
#             yield i**2
#     else:
#         for i in range(1,n+1):
#             yield i**3
# print(list(gen(int(input('enter number: ')))))