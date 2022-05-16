import numpy as np  #002 import numpy
#print(np.__version__) #003 numpy version

#vector = np.zeros(10) #004 your first vector
#print(vector)

#print(vector.size * vector.itemsize) #005 array memory size

#np.info(np.add) #006 numpy documentation

#vector = np.zeros(10) ##007 change vector values
#vector[4] = 1
#print(vector)

#vector = np.arange(10, 50) #008 vector ranging values
#print(vector)

#vector = np.arange(0, 10) #009 reverse vector
#vector = vector[::-1]
#print(vector)

#matriz = np.arange(0, 9).reshape((3, 3)) #010 matrix with ranging values
#print(matriz)

#arr = [1,2,0,0,4,0] #011 find indices of non zero elements
#print(np.nonzero(arr))

#identidad = np.eye(3) #012 identity matrix
#print(identidad)

#arr = np.random.random(3) #013 random values array
#print(arr)

#arr = np.random.random(10) #014 minimum and maximum
#print(max(arr))

#arr = np.random.random(10) #015 mean value
#print(np.mean(arr))

#matriz = np.ones((5,5)) #016 array border
#matriz[1:-1,1:-1] = "0"
#print(matriz)

#matriz = np.ones((5,5)) #017 add border to array
#print(np.pad(matriz, (1,1), 'constant', constant_values=(0, 0)))

#print(0 * np.nan) #018 result of expressions
#print(np.nan == np.nan)
#print(np.inf > np.nan)
#print(np.nan - np.nan)
#print(np.nan in set([np.nan]))
#print(0.3 == 3 * 0.1)

#matriz = np.arange(0, 9).reshape((3, 3)) #019 diagonal
#print(np.diag(matriz))

#matriz = np.zeros((8,8)) #20 checkerboard pattern
#matriz[1::2,::2] = 1
#matriz[::2,1::2] = 1
#print(matriz)