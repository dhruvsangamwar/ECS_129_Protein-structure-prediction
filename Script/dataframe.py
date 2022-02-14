import pdbCleanup as pc
import fxndefinitions as f
import numpy as np
from numpy.linalg import eig

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

# finding the average of the x coords in protein 1 and 2 (arr1 & 2)

N1 = np. size(xtil, 0)
N2 = np. size(ytil, 0)

# these two functions calculate the barycenter
f.findBarycenter(xtil, N1)
f.findBarycenter(ytil, N2)

# we now have the ~x_k(arr1) vectors and the ~y_k(arr2) vectors respectively

# this function will calculate all the 9 R values
R11 = R12 = R13 = R21 = R22 = R23 = R31 = R32 = R33 = 0
for i in range(0, N1):
    R11 += x[i][0] * y[i][0]
    R12 += x[i][0] * y[i][1]
    R13 += x[i][0] * y[i][2]
    R21 += x[i][1] * y[i][0]
    R22 += x[i][1] * y[i][1]
    R23 += x[i][1] * y[i][2]
    R31 += x[i][2] * y[i][0]
    R32 += x[i][2] * y[i][1]
    R33 += x[i][2] * y[i][2]

Matrix = np.array([[R11+R22+R33, R23-R32, R31-R13, R12-R21],
                   [R23-R32, R11-R22-R33, R12+R21, R13+R31],
                   [R31-R13, R12+R21, -R11+R22-R33, R23+R32],
                   [R12-R21, R13+R31, R23+R32, -R11-R22+R33]])

w, v = eig(Matrix)
print('E-value:', w)
print('E-vector', v)

# Now we will find the best fit RMSD using the steps below
