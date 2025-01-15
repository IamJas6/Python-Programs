#1. How to check whether the given number is even or not?
# n=int(input('enter number: '))
# if n%2==0:
#     print(n,'is even')

#2. WAP to check whether the given character is present inside given string or not if present print hehee else print
#hahaha
# s=input('enter string: ')
# c=input('enter character: ')
# if c in s :
#     print('hehee')
# else:
#     print('hahaha')

#3. WAP to check whether the given string is palindrome or not
# s=input('enter string: ')
# if s[::-1]==s:
#     print('palindrome')
# else:
#     print('not palindrome')

#4. WAP to check whether the ascii value of given character is divisible by 5 or not
# s=input('enter char: ')
# if ord(s)%5==0:
#     print('divisible')
# else:
#     print('not divisible')

#5. WAP to check whether the second character present inside the string i lower or not
# s=input('enter string: ')
# if 'a'<=s[1]<='z':
#     print('lower')
# else:
#     print('not lower')

#6. WAP to check whether given integer number is single digit or 2 digit or 3 digit or 4 digit or 5 digit or more than 5
# n=int(input('enter number: '))
# if 0<=n<=9:
#     print('single digit')
# elif 10<n<=99:
#     print('2 digit')
# elif 100<n<=999:
#     print('3 digit')
# elif 1000<n<=9999:
#     print('4 digit')
# elif 10000<n<=99999:
#     print('5 digit')
# else:
#     print('more than 5 digit')

#7. WAP to print Fizz if given integer number is divisible by 3, print buzz if integer number is divisible by 5,
#print fizz-buzz if integer number is divisible by both 3 & 5 else print it is not divisible by both 3 & 5
# n=int((input('enter number: ')))
# if n%3==0 and n%5==0:
#     print('fizz-buzz')
# elif n%3==0:
#     print('fizz')
# elif n%5==0:
#     print('buzz')
# else:
#     print('not divisible by both 3 & 5')

#8. WAP to check whether the given character is of alphabet or not, if alphabet then check whether it is lower case
# or not if lower case then check it is vowel or not
# c=input('enter char: ')
# if 'a'<=c<='z' or 'A'<=c<='Z':
#     if 'a'<=c<='z':
#         if c in 'aeiou':
#             print('vowel')
#         else:
#             print('not vowel')
#     else:
#         print('not lower')
# else:
#     print('not alphabet')

#9. WAP to check whether the given data is of mutable data type or not if mutable then check whether it is even or not
# if it is even then check whether second value is of float or not
# l=['a',1.8,9,4]
# if type(l) in [list, set, dict]:
#     if len(l)%2==0:
#         if type(l[1])==float:
#             print('even and float')
#         else:
#             print('even but not float')
#     else:
#         print('not even')
# else:
#     print('not mutable')

#10. WAP to check whether given number is divisible by both 3 & 5 or not by using nested if
# n=int(input('enter number: '))
# if n%3==0:
#     if n%5==0:
#         print('divisible by both')
#     else:
#         print('by 3 only')
# else:
#     if n%5==0:
#         print('by 5 only')
#     else:
#         print('not divisible by both 3 & 5')

#11. WAP to check whether the middle value present in the list is integer or not
# l=['a',1.5,6,9,'B']
# if len(l)%2==1:
#     if type(l[len(l)//2])==int:
#         print('middle value is integer')
#     else:
#         print('middle value is not integer')
# else:
#     print('it should be odd list to get middle value')