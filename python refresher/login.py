'''
#condition controlled
a=0
while a<5:
    print('*')
    a+=1

#count controlled
for num in range(5,10,2):
    print(num)

#collection controlled

list1=[1,2,3,45]
for i in list1:
    print (i)

import keyword
print(keyword.kwlist)

#delete object , use clear() just to empty w/o deleting

del(list1)

stat= "This is  not normal"
words =[]
for word in stat:
    words.append(word)

print(words)

#conditional statements

bro=int(input("Enter bro's age:"))
sis=int(input("Enter sis age:"))
if bro>sis:
    print("Bro's older")
elif sis>bro:
    print("Sis older")

else:
    print("The're same age")

#create a login acces using loop and condition

while True:
    choice=input("Choose option:")
    if choice =='log':
        id=input("Enter username:")
        passw=input("Enter password:")
        if id == "admin" and passw == "password":
            print("Login Successfull. Welcome")
        else:
            print("Incorrect credentials. Try again!")
    elif choice == 'exit':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Choose log or exit.")
'''
city = ['kochi',None,'tvm',None,'goa','hyd']

for i in city:
    if i == None:
        continue
    else:
        print(i)
               





