# file handling
'''
fileobj = open('file1.txt')
print(fileobj.read())

fileobj = open('file1.txt','r')
fileobj = open('file1.txt','w')
fileobj.write("This is new content")
fileobj.close()

fileobj1 = open('file2.txt','r+')
print(fileobj1.read())

print("Reading again..")
fileobj1.seek(0)
print(fileobj1.read())
'''
fobj = open("file2","w+")
print(fobj.read())
fobj.write("I am writing a predefined file.")
fobj.seek(0)
print(fobj.read())

with open('file2','r+') as fobj1:
    data = fobj1.readlines()
    for line in data:
        print(line)