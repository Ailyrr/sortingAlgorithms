#Swap Sorting Algorithm
def swap_sort(array):
    if(len(array) == 1):
        return True
    max_index = len(array) - 1
    while max_index > 0:
        for i in range(max_index):
            if(array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
        max_index-=1

#Tests
test_array = [29, 54, 13, 67, 82, 41, 95, 6, 18, 76, 23, 89, 37, 48, 10, 70, 92, 5, 30, 63];
swap_sort(test_array)
print(test_array)
