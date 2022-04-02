# recursive
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

# iterative
def binary_search_iterative(data, target, low, high):
    while True:
        if low > high:
            return False # return low (position to insert)
        else:
            mid = (low + high) // 2
            if target == data[mid]:
                return mid
            elif target < data[mid]:
                high = mid-1
            else:
                low = mid+1

print(binary_search([1,3,5,7,9],7,0,4)) # 3
print(binary_search_iterative([1,3,5,7,9],7,0,4)) # 3
