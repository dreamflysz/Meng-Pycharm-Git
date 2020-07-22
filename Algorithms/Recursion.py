# Given a string, find the first uppercase character.

import __init__
import os
import sys

input_str1 = 'liuMengfeiLoveCher'
input_str2 = 'liumengfeiLoveCher'
input_str3 = 'liumengfeilovecher'


def find_upper_iterative(inStr):
    for i in range(len(inStr)):
        if inStr[i].isupper():
            return inStr[i]
    return "no upper found"


def find_upper_recursive(inStr, i=0):
    if inStr[i].isupper():
        return inStr[i]
    if i == len(inStr) - 1:
        return "nonono upper"
    return find_upper_recursive(inStr, i + 1)


print(find_upper_iterative(input_str1))
print(find_upper_iterative(input_str2))
print(find_upper_iterative(input_str3))

print(find_upper_recursive(input_str1))
print(find_upper_recursive(input_str2))
print(find_upper_recursive(input_str3))

x = 500
y = 2000


def recursive_mul(x, y):
    if x < y:
        return recursive_mul(y, x)
    if y == 0:
        return 0
    return x + recursive_mul(x, y - 1)


print(x * y)
print(recursive_mul(x, y))

########################################################
