import numpy as np 
import matplotlib.pyplot as plt

array_1=np.random.randint(75,size=100)
array_1=array_1.reshape(50,2)
x=array_1[:,0]
y=array_1[:,1]
# plt.scatter(x,y)
plt.hist(x,y) 
plt.xlabel(x)
plt.ylabel(y)
plt.show()
