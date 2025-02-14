#Lambda

#1. WAP to check given char is present in given str or not
# l = lambda c,s : c in s
# print(l(s=input("enter string: "),c=input("enter char: ")))

#2. WAP to print sum of 3 numbers
# l = lambda n1,n2,n3 : n1+n2+n3
# print(l(n1=int(input('enter number: ')),n2=int(input('enter number: ')),n3=int(input('enter number: '))))

#3. WPA to find the product of minimum 3 numbers and maximum 5 numbers
# l = lambda n1,n2,n3,n4=1,n5=1 : n1*n2*n3*n4*n5
# print(l(n1=int(input('enter number: ')),
#         n2=int(input('enter number: ')),
#         n3=int(input('enter number: ')),
#         n4=int(input('enter number: ')),
#         n5=int(input('enter number: '))
# ))

#4. WAP to check given character is of special character or not
# l = lambda c: not('A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9')
# print(l(c=input('enter char: ')))
# if l(c=input('enter char: ')) == True:
#     print('Special')
# else:
#     print('Not special')

#5. WAP to check given integer number is divisible by 3 or not
# l = lambda n: n%3==0
# print(l(n=int(input('enter number: '))))


#Map
#1. WAP to find sum of individual digits of all the integer numbers present in homogenous list collection
# def sum(n):
#     s=0
#     for i in str(n):
#         s+=int(i)
#     return s
# l=[12,34,56,78,90]
# li=list(map(sum,l))
# print(li)

#2.WAP to find the factorial of all integer numbers present in homogenous list collection
# def fact(n):
#     f=1
#     i=1
#     while i<=n:
#         f*=i
#         i+=1
#     return f
# print(list(map(fact,[6,3,2])))

#3. WAP find square of all the integer numbers present in range 1 to 10 by lambda and map
# print(list(map(lambda s:s**2, range(1,11))))

#4. WAP to add 10 to all the numbers present from range 20 to 30
# print(list(map(lambda s:s+10, range(20,31))))

#5. WAP to store the length of all the string data present in homogenous list collection
# print(list(map(lambda s:len(s),['suhail','uddin','yasir'])))