import numpy as np

ar1 = np.array([10,20,30,40,50,70])
print(ar1)
print(ar1.shape)
print(ar1.dtype)
print(ar1.itemsize)
print(ar1.size)
print(ar1.ndim)
print(ar1.nbytes)

ar2=np.array([[10,29,39,40],
            [18,11,23,23],
            [20,34,52,62]])
print(ar2.shape)

#slicing and indexing

print(ar2[1:-1,1:-1])  #first and last row and coloumn ignored since it starts from 1 to -1, hence only center

ar3=np.array([[[10,29,39,40],
            [18,11,23,23],
            [20,34,52,62]],

            [[10,40,39,20],
            [18,13,53,23],
            [20,34,54,62]]])
print(ar3.shape)
print(ar3[1,1,2])
print("\n")
# create numpy array using functions

ar4=np.arange(1,10).reshape(3,3)  
# arrange - function to create arrays 
#reshape can be used to rershape 1D array to other dimetions (3,3) or (2,5,5)

print(ar4)

ar5=np.zeros((5,5))  #by default its in float , can be made into int { dtype="int16"  }
print(ar5)

print("\n")
ar6=np.identity(5)
print(ar6*5)

print(np.full((2,3),3)) # can be used to create and fill a new array with a value (shape,value)

#linspace
# creates an array with equally spaced numbers (space,max,no. of stopes)

print(np.linspace(5,50,10,dtype='int16')) 

#logspace
# creates evenly spaced log scale b/w two number

#Exersice 1  : Bordered box
ar7=(np.full((10,10),1))
ar7[1:-1,1:-1].fill(0)    #also  ar7[1:-1,1:-1] = 0
print(ar7)

#Exersice 2  : Checked box
print("\n")
ar8=(np.full((10,10),1))
ar8[::2,::2].fill(0)
ar8[1::2,1::2].fill(0)      # require 2 slicing for checkered box : two alternate replacing of 0 
print(ar8)

print(ar8.sum())



ar9=np.array([[[10,29,39,40],
            [18,11,23,23],
            [20,34,52,62]],

            [[10,40,39,20],
            [18,13,53,23],
            [20,34,54,79]]])

print(ar9.sum())
print(ar9.sum(axis=0))  #row wise summing : matrix addition
print(ar9.sum(axis=1)) # coloumn wise addition : adds couloums of each matrix

print(ar9.min())
print(ar9.max())
#print(np.where(ar9 > 15)) # where : shows the index values of elements where condtion satisfies

ar10=np.arange(1,37).reshape(6,6)
print(ar10)
print(ar10.mean(axis=0))  # mean row wise
print(ar10.mean(axis=1))  # mean coloumn 

# reversing

print(np.flip(ar10))
# can also use lrflip(), udflip(), lrflip()

# flatten :  N-D array  to 1-D array
# revel() does the same

ar11=np.random.randint(10,99, size=(5,3))
print(ar11.flatten())

print(np.argmax(ar9))  # retuerns index position of maximum along the axis