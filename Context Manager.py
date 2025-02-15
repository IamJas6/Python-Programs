#This is normal open close of file in which if any error raises it wont handle 
# file = open('sample.txt','w')
# try:
#     file.write('This is a sample text file.')
# finally:
#     file.close()


#This is context manager where it will handle all of the errors that happen in open and close
# with open('sample.txt','w') as f:
#     f.write('This is a sample text file.')
