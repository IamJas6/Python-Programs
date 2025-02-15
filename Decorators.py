#User defined decorators
#syntax:
    #def dname(func):
        #def inner():
            #operation before main task
            #func()
            #operation after main task
        #return inner
    #@dame
    #def fname(args):
    #   statement

#1.WAP to calculate total time taken to find square of the numbers from range 1 to 100
# import time
# st = time.time()
# for i in range(1,101):
#     print(i)
# et = time.time()
# print(et-st)

#2. WAP to calculate total time taken to print the sum of 2 integers
# def timer(func):
#     def inner():
#         import time
#         st = time.time()
#         func()
#         et = time.time()
#         print(et-st)
#     return inner

# @timer
# def sum():
#     n1=int(input('enter number1: '))
#     n2=int(input('enter number2: '))
#     print(n1+n2)
# sum()


#----------------OR-------------#
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print(f"Time taken by function {func.__name__}: {end_time - start_time} seconds")
    return wrapper

@timer
def cal_sum(n):
    return sum(range(n))
print(cal_sum(10))
    