data = [2, 3, 22, 4]
target = 3


# Linear Search

def liner_search(d, t):
    for i in range(len(d)):
        if d[i] == t:
            return True
    return False


print(liner_search(data, target))


# Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Recurseive Binary Search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)

        else:
            return binary_search_iterative(data, target, mid - 1, high)


print(binary_search_iterative(data, target))
