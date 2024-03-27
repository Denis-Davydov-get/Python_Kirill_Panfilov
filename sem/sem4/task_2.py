# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def text_new_line(text):
    res_array = []
    for value in text:
        res_array.append(ord(value))
    return set(res_array)

print(text_new_line('Traceback'))