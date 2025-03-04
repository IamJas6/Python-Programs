#[A-Z]
#[a-z]
#[0-9] or \d

#[A-Z a-z 0-9] or \w

# ? = 0 or 1 char
# + = 1 to n char
# * = 0 to n char
# \ = remove special behaviour

# [A-Z]{n}
# [A-Z]{m,n}

#1. WAP to match indian phone number 
# \+91[6-9][0-9]{9}
#or
# \+91[6-9]\d{9}

# import re
# pattern = r'\+91[6-9]\d{9}'
# phone = input('Enter your phone number: ')
# if re.match(pattern, phone):
#     print(f'{phone} - Valid Indian Phone Number')
# else:
#     print('Invalid Indian Phone Number')


#2. WAP to find unique student id
#example : A123
#[A-Z][0-9]{3}  or [A-Z]\d{3}
# import re
# pattern = r'[A-Z]\d{3}'
# id = input('enter your id: ')
# if re.match(pattern, id):
#     print(f'{id} - Valid Student ID')
# else:
#     print('Invalid Student ID')


#3. WAP to match adhaar address
#\d{4\ \d{4}\ \d{4}
# import re
# pattern = r'\d{4}\ \d{4}\ \d{4}'
# adhar = input('enter adhaar number: ')
# if re.match(pattern, adhar):
#     print(f'{adhar} - Valid Adhaar Number')
# else:
#     print('Invalid Adhaar Number')

#4. WAP to match email address
#example: dinga.qsp1@gmail.com
# import re
# pattern = r'[A-z a-z 0-9]+\.?[A-Z a-z 0-9]+@[A-z a-z]+\.[a-z]{2,3}'
# email = input('Enter your email: ')
# if re.match(pattern, email):
#     print(f'{email} - Valid Email')
# else:
#     print('Invalid Email')

#5. WAP extract date
#example: today is 05-01-2025, adn 04-01-2025
#output: ['05-01-2025','04-01-2025']
# import re
# pattern = r'\d{2}-\d{2}-\d{4}'
# dates = input('Enter data: ')
# if re.findall(pattern, dates):
#     print(re.findall(pattern, dates))
# else:
#     print('No date found')