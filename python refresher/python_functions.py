from functools import reduce
from collections import defaultdict

'''
def greet():
    return "helloo"
s=greet()
print(s)

multi = lambda a:a*2  # declare with an argument
print(multi(2))

# inbuild function

num=[1,2,3,4,5]

pow= list(map(lambda a:a**2,num))
even= list(filter(lambda a:a%2==0,num))
sum= reduce(lambda x,y:x+y,num )

print(pow)
print(even)
print(sum)
'''

#create a funtion and apply on reduce to return aggregate sales data

sales=[{'Product':'lap','amt':50000},
       {'Product':'phone','amt':55000},
       {'Product':'tv','amt':40000},
       {'Product':'mouse','amt':400},
       {'Product':'tv','amt':60000},
       {'Product':'lap','amt':70000},
       {'Product':'phone','amt':30000}
       ]
#total accumulate sales revenue for each product
def accumulate(acc,trans):
    product = trans["Product"]
    amount = trans["amt"]
    acc[product]+=amount
    return acc

#reduce(function,iterable,intializer)

tot_sales= reduce(accumulate,sales,defaultdict(int))
print(tot_sales)
        
#find top selling product and top selling revenue
top_prod=max(tot_sales,key=tot_sales.get)
top_rev=tot_sales[top_prod]

for product,revenue in tot_sales.items():
    print(f"{product}:{revenue}")

print(f"Top selling product :{top_prod} with value {top_rev}")

# *args and **kwargs


def demo(*args):
        tot=sum(args)
        return tot
A=[1,2,3,4,5]
print(demo(*A))

def emp_info(**kwargs):
     for key,value in kwargs.items():
          print(f"{key}:{value}")

emp_info(name="elias",age=22,city="kochi")

print





