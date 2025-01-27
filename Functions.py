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

#9. WAP 