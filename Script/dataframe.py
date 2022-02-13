import pdbCleanup as pc
import numpy as np


pc.takeInput1()
DataFrame1 = []
pc.CsvToDataframe(DataFrame1)

pc.takeInput2()
DataFrame2 = []
pc.CsvToDataframe(DataFrame2)

arr1 = np.array(DataFrame1)
arr2 = np.array(DataFrame2)

input("This is the first protein:")
print(arr1[0])


input("This is the second protein:")
print(arr2[0])


# finding the average of the x coords in protein 1 and 2 (arr1 & 2)

def findBarycenter(array, N):
    sumx = 0
    for x in range(0, N):
        sumx += array[x][0]

    sumx = sumx/N
    # print(sumx)

    for x in range(0, N):  # appending the x vals
        array[x][0] -= sumx

    # finding the average of the y coords in protein 1
    sumy = 0
    for y in range(0, N):
        sumy += array[y][1]

    sumy = sumy/N
    # print(sumx)

    for y in range(0, N):  # appending the y vals
        array[y][1] -= sumy

    # finding the average of the z coords in protein 1
    sumz = 0
    for z in range(0, N):
        sumz += array[z][2]

    sumz = sumz/N
    # print(sumz)

    for z in range(0, N):  # appending the z vals
        array[z][2] -= sumz

    print("This is the appended array:")
    print(array[0])


N1 = np. size(arr1, 0)
N2 = np. size(arr1, 0)
findBarycenter(arr1, N1)
findBarycenter(arr2, N2)

# we now have the ~x_k(arr1) vectors and the ~y_k(arr2) vectors respectively
