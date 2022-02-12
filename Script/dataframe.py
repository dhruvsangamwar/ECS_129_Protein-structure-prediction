import os
import pandas as pd
import pdbCleanup
import numpy as np
import csv

DataFrame1 = []
DataFrame2 = []

with open("protein1.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        DataFrame1.append(row)


with open("protein2.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        DataFrame2.append(row)

arr1 = np.array(DataFrame1)
arr2 = np.array(DataFrame2)

input("This is the first protein:")
print(arr1[0])


input("This is the second protein:")
print(arr2[0])

# finding the average of the x coords in protein 1 (arr1)
sumx = 0
for x in range(0, 134):
    sumx += arr1[x][0]

sumx = sumx/134
# print(sumx)

for x in range(0, 134):  # appending the x vals
    arr1[x][0] -= sumx

# finding the average of the y coords in protein 1
sumy = 0
for y in range(0, 134):
    sumy += arr1[y][1]

sumy = sumy/134
# print(sumx)

for y in range(0, 134):  # appending the y vals
    arr1[y][1] -= sumy

# finding the average of the z coords in protein 1
sumz = 0
for z in range(0, 134):
    sumz += arr1[z][2]

sumz = sumz/134
# print(sumz)

for z in range(0, 134):  # appending the z vals
    arr1[z][2] -= sumz

print("This is the appended array 1")
print(arr1)


# finding the average of the x coords in protein 2 (arr2)
sumx = 0
for x in range(0, 134):
    sumx += arr2[x][0]

sumx = sumx/134
# print(sumx)

for x in range(0, 134):  # appending the x vals
    arr2[x][0] -= sumx

# finding the average of the y coords in protein 1
sumy = 0
for y in range(0, 134):
    sumy += arr2[y][1]

sumy = sumy/134
# print(sumx)

for y in range(0, 134):  # appending the y vals
    arr2[y][1] -= sumy

# finding the average of the z coords in protein 1
sumz = 0
for z in range(0, 134):
    sumz += arr2[z][2]

sumz = sumz/134
# print(sumz)

for z in range(0, 134):  # appending the z vals
    arr2[z][2] -= sumz

print("This is the appended array 2")
print(arr2)

# we now have the ~x_k vectors and the ~y_k vectors respectively

# at the end of this sequence the program will remove the csv files

os.remove("protein1.csv")
os.remove("protein2.csv")
