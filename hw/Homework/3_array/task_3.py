# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Input:
# lst = [1_base, 1_base, 2_type_data, 2_type_data, 3_array, 3_array] # test 1_base
lst = [1, 2, 3, 2, 4, 5, 4]  # test 3_array


# lst = [1_base, 1_base, 1_base, 1_base, 1_base] # test 4_func
# Output:
# [1_base, 2_type_data, 3_array]

def del_copy(lst):
    """function search duplicate and append new array"""
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

print(del_copy(lst))


