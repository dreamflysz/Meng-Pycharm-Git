def countE_O(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [-2, 4, 5, 6, 77, 8, 445, 6, 78, -4]

e, o = countE_O(lst)

print(e)
print(o)

print("{}     {}".format(e, 0))
