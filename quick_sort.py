#Quick Sort Algorithm
def quick_sort(array):
    if len(array) <= 1:
        return array
    #Define Pivot
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#Tests
test_array = [29, 54, 13, 67, 82, 41, 95, 6, 18, 76, 23, 89, 37, 48, 10, 70, 92, 5, 30, 63]
sorted = quick_sort(test_array)
print(sorted)