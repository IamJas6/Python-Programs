#Specific Exception
#Generic Exception
#Default Exception

#specii exception
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print('cannot divide by zero')

#generic exception
# try:
#     print(10/0)
# except Exception as e:
#     print(e)

#default exception
# try:
#     print(10/0)
# except:
#     print('something went wrong')

# All in one example
# def exception_demo(choice):
#     try:
#         if choice == 1:
#             # Specific Exception: ZeroDivisionError
#             result = 10 / 0  
#         elif choice == 2:
#             # Specific Exception: FileNotFoundError
#             with open("non_existent_file.txt", "r") as file:
#                 content = file.read()
#         elif choice == 3:
#             # Specific Exception: ValueError
#             num = int("abc")  # Trying to convert a string to an integer
#         elif choice == 4:
#             # Generic Exception: Trying an invalid operation
#             lst = [1, 2, 3]
#             print(lst[10])  # IndexError
#         else:
#             # Default Exception: No exception handling
#             print("No exception triggered.")

#     except ZeroDivisionError as e:
#         print(f"Specific Exception Caught: {e}")
#     except FileNotFoundError as e:
#         print(f"Specific Exception Caught: {e}")
#     except ValueError as e:
#         print(f"Specific Exception Caught: {e}")
#     except Exception as e:
#         print(f"Generic Exception Caught: {e}")

# # Test cases
# print("Case 1: ZeroDivisionError")
# exception_demo(1)

# print("\nCase 2: FileNotFoundError")
# exception_demo(2)

# print("\nCase 3: ValueError")
# exception_demo(3)

# print("\nCase 4: Generic Exception (IndexError)")
# exception_demo(4)

# print("\nCase 5: No Exception")
# exception_demo(5)
