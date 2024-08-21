list1 = []
for i in range(1,11):
    if i % 2 == 0:
        list1.append(i**2)
print(list1)

list2 = [i**2 for i in range(1,11) if i%2==0]

# grade
marks=[80,50,45,95,75]
grade=[(lambda x: 'S' if x>=90 else 'A' if x>=80 else 'B' if x>=70 else 'C' if x>=50 else 'F')
       (mark) for mark in marks]
print(grade)