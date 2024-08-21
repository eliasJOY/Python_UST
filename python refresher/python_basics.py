str1='This is a trial text for python'
print((str1[::-1]))  #string reverse
print(str1)

str2=str.lower(str1)
print('The position on python is {}'.format(str2.find('python')))

A=["elias","joy"]
print(" ".join(A))

#inp=int(input("Enter something:"))
inp=10
print(f"A number is {inp}")

stripped=str1.lstrip()
print(stripped)

print(str1.rpartition(" "))  #delimiter can be , space, etc

A=['hi','we','are','learning']
A.append("python")

print(A)

#shallow copy - only values
B=A.copy()
#deep copy - copy by reference
C=A
A.append('program')
print(B)
print(C)

A.extend(['and','some','other','things'])

#tuples iterate faster to list - list manages two memory while tuple only manage one

# SETS -  unordered collection of data with no indexes.
set1=set()

set1={'a','b','c','d'}
set2={'a','b','e'}

print(set1.difference(set2))

print(set1)
set1.pop()  #random
print(set1)

set1.update('y','z') #updates a set by group of elements
print(set1)

print(set1.symmetric_difference(set2)) #union of two sets not common in both sets


#dict

dict1={}
dict1 = {'A':'App','B':'Blue','C':'Car','D':'Donut'}  #METHOD 1
data=[1,2,3,4]
city = ['kochi','tvm','goa','hyd']
dict2 = dict1.fromkeys(city,50)
print(dict2)

dict3=dict(zip(city,data))  #METHOD 2
print(dict3)

dict4=dict([('kochi',20),('tvm',30),('goa',40)]) #METHOD 3
print(dict4)

for key in dict4.items():
    print(key)

dict5={}
for k,v in enumerate(city,start=1):
    print(f"Index: {k} : Keys:{v}, Value= {dict5[k]}")