# Set Comprehension

#1. WAP to find square of all integer numbers from range 1 to 10 and store output in set
# print({i**2 for1 i in range(1,11)})

#2. WAP to extract all numbers whos ascii value is even from given string
# print({i for i in 'suha968il' if '0'<=i<='9' and ord(i)%2==0})

#3. WAP to extract all the complex data present in heterogenous list
# print({i for i in ['a',2+3j, 2, 2.2] if type(i)==complex})

#4. WAP to print all divisors of given integer number
# print({i for i in range(1,10) if 10%i==0})

#5. WAP to print sum of first 10 natural numbers 
# s=0
# print({(s:= s+i) for i in range(1,11)})


#Zip Function
# Example 
# for i,j in zip([1,2,3], [1,2,3]):
#     print(i,j)


#Dictionary Comprehension

#1. WAP to map 2 strings in form of dictionary
# print({i:j for i,j in zip('Hi', 'Suhail')})

#2. WAP create a dictionary by considering 2 heterogenous list collection where key should be integer
# print({i:j for i,j in zip([1,'a',3], ['Mohammed', 'Suhail', 'uddin']) if type(i)==int})

#3. WAP to create a dictionary where key should be integer and value should be of any collection with length >= 3 
# by considering 2 heterogenous list
# print({i:j for i,j in zip([1,2,3,4], ['abc','bca','cab','dcb']) if type(i)==int and len(j)>=3 and type(j) in [str, list, tuple, dict, set]})

#4. WAP to create a dictionary value should be of square of its original value by considering homogenous list
# print({i:j**2 for i,j in zip([1,2,3,4], [1,2,3,4])})