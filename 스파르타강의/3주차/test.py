finding_target = 16
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
def is_existing_target_number_binary(target, array):
    middle_num_index = len(array) // 2 # array[8] = 9
    print(array[middle_num_index], middle_num_index)
    if array[middle_num_index] == target:
        return True
    if array[middle_num_index] < target:
        print(array[middle_num_index+1:])
        return is_existing_target_number_binary(target, array[middle_num_index+1:])
    else:
        print(array[:middle_num_index])
        return is_existing_target_number_binary(target, array[:middle_num_index])
    return False
result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)