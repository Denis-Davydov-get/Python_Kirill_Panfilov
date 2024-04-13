# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# 10 гласных букв: а, о, у, ы, э, я, е, ё, ю, и;
# 21 согласная буква: б, в, г, д, й, ж, з, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ;
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random

MIN_LEN = 4
MAX_LEN = 7


def gen_name(count_num: int, file_num: str):
    with open(file_num, 'a', encoding='utf-8') as f:
        while count_num:
            name = ''
            name_len = random.randint(MIN_LEN, MAX_LEN) #
            vowels = 'аоуыэяеёюи'  # гласные
            consonant_letter = 'бвгдйжзклмнпрстфхцчшщ'  # согласные
            for _ in range(name_len):
                name += (f'{random.choice(consonant_letter)}{random.choice(vowels)}')
            count_num -= 1
            return f.write(f'{name.capitalize()}\n')


gen_name(5, 'test.txt')
