# #Write Mode
# file = open('test.txt','w')
# file.write('Hi this is testing of write mode.')

# #Read Mode
# file = open('test.txt','r')
# read = file.read()
# print(read)

# #Append Mode
# file = open('test.txt','a')
# file.write(' This is apending test')
# file = open('test.txt','r')
# read = file.read()
# print(read)

#Pickling
#1. Json Pickling
    #a.Encryption
    #b.Decryption

#Encryption
# from json import dumps as d
# file = open('test1.txt','w')
# data = 'This is encryptioning data'
# endata = d(data)
# file.write(endata)

# #Decryption
# from json import loads 
# file = open('test1.txt','r')
# data = file.read()
# dedata = loads(data)
# print(dedata)

#2. Pickling
    #a. Uppickling
    #b. Downpickling

#Uppickling
# import pickle
# file = open('test2.txt','wb')
# data = 'This is up pickling'
# endata = pickle.dumps(data)
# file.write(endata)

#Downpickling
# file = open('test2.txt','rb')
# data = file.read()
# dedata = pickle.loads(data)
# print(dedata)