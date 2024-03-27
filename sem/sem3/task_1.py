# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка

list_1 = [1, 5, 8, 1, 56, 3, 4, 6, 5, 4]
def del_copy(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(del_copy(list_1))
print(set(list_1))