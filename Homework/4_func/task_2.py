# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Input:
# params = key_params(a=1_base, b='hello', c=[1_base, 2_type_data, 3_array], d={})
# print(params)
# Output:
# {1_base: 'a', 'hello': 'b', '[1_base, 2_type_data, 3_array]': 'c', '{}': 'd'}

def key_params(**kwargs):
    res = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            res[value] = key
        except TypeError:
            res[str(value)] = key
    return res
