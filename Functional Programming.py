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
