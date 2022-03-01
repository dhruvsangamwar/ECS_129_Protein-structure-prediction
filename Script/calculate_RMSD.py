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

xtil = [0, 0, 0]
ytil = [0, 0, 0]

x = np.array(DataFrame1)
y = np.array(DataFrame2)

# This finds the number of CA atoms in both of the proteins

N1 = np.size(xtil, 0)
N2 = np.size(ytil, 0)

# finding the average of the x coords in protein 1 and 2 (arr1 & 2)
# these two functions calculate the barycenter

# Here we will be finding Xtil && Ytil = X && Y - G

Gx = f.findG(x, N1)
Gy = f.findG(y, N2)

xtil = np.subtract(x, Gx)
ytil = np.subtract(x, Gy)

# we now have the ~x_k Coords and the ~y_k Coords respectively

# this function will calculate all the 9 R values
R11 = R12 = R13 = R21 = R22 = R23 = R31 = R32 = R33 = 0

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

# Here we calculate the maxEigenvalue for the final calucaltion

w, v = eig(Matrix)
maxEig = np.amax(w)

# Now we will find the best fit RMSD using the steps below

temp = [0, 0, 0]
for i in range(0, N1):
    temp += np.add((np.square(xtil[i])), np.square(ytil[i]))

n = temp[0] + temp[1] + temp[2]

almostfinal = np.subtract(n, 2*maxEig)

temp2 = np.true_divide(almostfinal, np.size(xtil, 0))
RMSD = np.sqrt(abs(temp2))
RMSD = round(RMSD, 2)
print(RMSD)
