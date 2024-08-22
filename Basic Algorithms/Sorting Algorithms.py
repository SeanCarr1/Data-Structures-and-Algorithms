import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i - 1):
            next = arr[j+1]
            current = arr[j]

            if current > next:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr

def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1

    return arr

def selection_sort(arr):
    for i in range(len(arr)-2):
        curr_min = i
        for j in range(i+1, len(arr)-1):
            if arr[j] < arr[curr_min]:
                curr_min = j
        if curr_min != i:
            arr[j], arr[curr_min] = arr[curr_min], arr[j]

    return arr

class MergeSort:
    def __init__(self) -> None:
        pass

    def merge_sort(self, array):
        if len(array) == 1:
            return array
        
        mid = len(array) // 2
        left_arr = array[:mid]
        right_arr = array[mid:]

        sorted_left = self.merge_sort(left_arr)
        sorted_right = self.merge_sort(right_arr)

        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result
 
class QuickSort:
    def __init__(self) -> None:
        pass

    def quick_sort(self, array, low=0, high=None):
        if high == None:
            high = len(array) - 1

        if low < high:
            pivot_index = self.partition(array, low, high)
            self.quick_sort(array, low, pivot_index - 1) #left
            self.quick_sort(array, pivot_index+1, high) #right
        
        return array

    def partition(self, array, low, high):
        pivot = array[high]
        i = low-1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
            
        array[i+1], array[high] = array[high], array[i+1]
        return i + 1




array = random.sample(range(0, 10000), 10)

def measure_time(arr, func):
    start_time = time.time()
    arr = func(arr)
    print(f"{(time.time()-start_time)} seconds: --- {arr[0:10]}")

# measure_time(array, bubble_sort)
# measure_time(array, insertion_sort)
# measure_time(array, selection_sort)
# measure_time(array, MergeSort().merge_sort)

print(QuickSort().quick_sort(array, 0, len(array) - 1))

