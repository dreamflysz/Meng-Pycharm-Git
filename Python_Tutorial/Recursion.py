from functools import reduce


# import sys
#
# sys.setrecursionlimit(20)
#
# print(sys.getrecursionlimit())
#
# i = 0
#
# def greet():
#
#     global i
#     i += 1
#
#     print("Mengfei succeeds" , i)
#     greet()
#
# greet()

def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)


print(fact(3))

f = lambda a, t: a * 8 + t  # Lambda, anonymous function keyword

result = f(4, 2)

nums = [2, 23, 44]

w = list(filter(lambda n: n % 2 == 0, nums))

print(w)

# def add_all(a,b):
#     return a + b

sum = reduce(lambda x, y: x + y, nums)

print(sum)


def div(a, b):
    if a < b:
        a, b = b, a
    print(a / b)


div(3, 11)
