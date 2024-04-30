#Merge Sort Algorithm
def merge(left_array, right_array):
    out_list = []
    left_ptr, right_ptr = 0, 0
    
    # Compare elements from both halves and merge them
    while left_ptr < len(left_array) and right_ptr < len(right_array):
        if left_array[left_ptr] < right_array[right_ptr]:
            out_list.append(left_array[left_ptr])
            left_ptr += 1
        else:
            out_list.append(right_array[right_ptr])
            right_ptr += 1
            
    # Add any remaining elements from the left and right halves
    out_list.extend(left_array[left_ptr:])
    out_list.extend(right_array[right_ptr:])
    
    return out_list

def merge_sort(array):
    if(len(array) == 1):
        return array

    midpoint = len(array) // 2
    left_part = merge_sort(array[:midpoint])
    right_part = merge_sort(array[midpoint:])

    return merge(left_part, right_part)
    

#Tests
test_array = [29, 54, 13, 67, 82, 41, 95, 6, 18, 76, 23, 89, 37, 48, 10, 70, 92, 5, 30, 63];
print("Sorted: ", merge_sort(test_array))