#Bubble Sort Algorithm
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Tests
test_array = [29, 54, 13, 67, 82, 41, 95, 6, 18, 76, 23, 89, 37, 48, 10, 70, 92, 5, 30, 63];
bubble_sort(test_array)
print("Sorted: ", test_array)