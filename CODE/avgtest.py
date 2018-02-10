import numpy

arr = [0, 0, 0, 0]
for x in range(0, 50):
    print x, " ", numpy.mean(arr)
    arr = []
    for a in range(0, 4):
        arr.append(a)
        a = a + 1
