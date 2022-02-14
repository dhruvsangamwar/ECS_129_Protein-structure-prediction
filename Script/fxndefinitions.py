
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
