import pdbCleanup as pc
import fxndefinitions as f
import numpy as np
from numpy.linalg import eig
import math

pc.takeInput1()
DataFrame1 = []
pc.CsvToDataframe(DataFrame1)

pc.takeInput2()
DataFrame2 = []
pc.CsvToDataframe(DataFrame2)

xtil = np.array(DataFrame1)
ytil = np.array(DataFrame2)

x = np.array(DataFrame1)
y = np.array(DataFrame2)

N1 = np.size(xtil, 0)
N2 = np.size(ytil, 0)
# finding the average of the x coords in protein 1 and 2 (arr1 & 2)

#N1 = np.size(xtil, 0)
#N2 = np.size(ytil, 0)

# these two functions calculate the barycenter
f.findBarycenter(x, y, xtil, N1)
f.findBarycenter(x, y, ytil, N2)

# f.calculateG(x, y, xtil, N1) ignore this fxn, I was just testing how G is being calculated

# we now have the ~x_k(arr1) vectors and the ~y_k(arr2) vectors respectively

# this function will calculate all the 9 R values
R11 = R12 = R13 = R21 = R22 = R23 = R31 = R32 = R33 = 0

# print(x[0][0])
# print(y[0][0])
# print(np.size(xtil, 0))
# print(np.size(ytil, 0))

for i in range(0, N1):
    R11 += xtil[i][0] * ytil[i][0]
    R12 += xtil[i][0] * ytil[i][1]
    R13 += xtil[i][0] * ytil[i][2]
    R21 += xtil[i][1] * ytil[i][0]
    R22 += xtil[i][1] * ytil[i][1]
    R23 += xtil[i][1] * ytil[i][2]
    R31 += xtil[i][2] * ytil[i][0]
    R32 += xtil[i][2] * ytil[i][1]
    R33 += xtil[i][2] * ytil[i][2]

# matrix given by equation 10 from the paper

Matrix = np.array([[R11+R22+R33, R23-R32, R31-R13, R12-R21],
                   [R23-R32, R11-R22-R33, R12+R21, R13+R31],
                   [R31-R13, R12+R21, -R11+R22-R33, R23+R32],
                   [R12-R21, R13+R31, R23+R32, -R11-R22+R33]])
print(Matrix)

w, v = eig(Matrix)
print('E-value:', w)
maxEig = np.amax(w)
print('MAX E-value:', maxEig)


# Now we will find the best fit RMSD using the steps below
print(ytil[0])
temp = [0, 0, 0]
for i in range(0, N1):
    temp += np.add((np.square(xtil[i])), np.square(ytil[i]))

temp = np.subtract(temp, 2*maxEig)
temp2 = np.true_divide(temp, np.size(xtil, 0))
print(temp2)
RMSD = np.sqrt(abs(temp2))

print(RMSD)
