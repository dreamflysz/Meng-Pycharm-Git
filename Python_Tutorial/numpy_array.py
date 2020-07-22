from numpy import *

arr = array([1, 2, 3, 4, 5], int)

arr2 = arr.copy()

arr[1] = 33

mularray = array([

    [1, 2, 3, 7, 223, 0.9],
    [3, 4, 55, 17, 0.067, -112]

])

m = matrix('1 3 -9; 2 8 0')

mularray1 = mularray.flatten()
mularray2 = mularray1.reshape(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
                              3)

print(m.max())

print(arr.dtype)
print(arr)
print(arr2)

arr1 = ones(5, int)

print(id(arr1))
print(id(arr))

print(concatenate([arr1, arr]))


def add_sub(x, y):
    c = x + y
    m = x - y
    return m, m


result1, result2 = add_sub(3, 8)
print(result1, result2)
