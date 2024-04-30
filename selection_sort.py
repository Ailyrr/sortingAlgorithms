#Selection Sort Algorithm
def selection_sort(array):
    if(len(array) == 1):
        return True
    for start_index in range(len(array)):
        for i in range(start_index + 1, len(array)):
            if array[start_index] > array[i]:
                array[i], array[start_index] = array[start_index], array[i]


#Tests
test_array = [29, 54, 13, 67, 82, 41, 95, 6, 18, 76, 23, 89, 37, 48, 10, 70, 92, 5, 30, 63];
selection_sort(test_array)
print("Sorted: ", test_array)