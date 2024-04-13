# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
# Input:
text = 'Hello world. Hello Python. Hello again.'
# Output:
# [('hello', 3_array), ('world', 1_base), ('python', 1_base), ('again', 1_base)]

text = text.lower()
new_text = ''
for i in text:
    if not i.isspace() and not i.isalpha():
        i = ' '
    new_text += ''.join(i)
new_text = new_text.split()
res_lst = []
for i in new_text:
    res_lst.append((i, new_text.count(i)))
res_lst = list(set(res_lst))
res_lst = sorted(res_lst, key=lambda x: (x[1], x[0]), reverse=True)
print(res_lst)
