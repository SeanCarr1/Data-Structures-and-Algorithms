import random

def binary_search(arr, val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == val:
            return mid
        if val > arr[mid]:
            left = mid+1
        if val < arr[mid]:
            right = mid-1
    
    return -1

array = random.sample(range(0, 100), 10).sort()
print(array)
