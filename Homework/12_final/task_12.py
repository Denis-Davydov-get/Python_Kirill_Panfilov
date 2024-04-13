import csv


class Student:
    subjects = {}  # предметы

    def __init__(self, name, subjects_file):
        """Класс Student принимает
        @ name: Имя Фамилия студента
        @ subjects_file: файл где искать студента по имени фамилии"""
        self.name = name
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        """Метод принимает Имя и путь к файлу, проверяет чтобы имя было из букв и начиналось
        с заглавной буквы, иначе выдает ошибку с предупреждением
        Output:
        Экземпляр класса с измененными параметрами"""
        if name == 'name':
            if not all(word.isalpha() and word[0].isupper() for word in value.split(' ')):
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
            super().__setattr__(name, value)

    def __getattr__(self, name):
        '''Выводит предмет, если он есть'''
        if name in self.subjects:
            return True
        else:
            raise ValueError(f"Предмет {name} не найден")

    def __str__(self):
        subjects = []
        for subject, score in self.subjects.items():
            if score['grade'] or score['test_score']:
                subjects.append(subject)
        return f"Студент: {self.name}\nПредметы: {', '.join(subjects)}"

    @classmethod
    def load_subjects(cls, subjects_file):
        """Метод класса. Чтение из файла для получения словаря для передачи в конструктор класса Student
        @ subjects_file - путь к файлу
        Output:
        subject(Предмет): grade(Оценка), test_score(результат теста)"""
        with open(subjects_file, "r") as file:
            for row in csv.reader(file):
                for subject in row:
                    cls.subjects[subject] = {"grade": [], "test_score": []}

    def add_grade(self, subject, grade):
        if self.__getattr__(subject):
            if not isinstance(grade, int) or not (2 <= grade <= 5):
                raise ValueError("Оценка должна быть целым числом от 2 до 5")
            else:
                self.subjects[subject]['grade'].append(grade)

    def add_test_score(self, subject, test_score):
        if self.__getattr__(subject):
            if not isinstance(test_score, int) or not (0 <= test_score <= 100):
                raise ValueError("Результат теста должен быть целым числом от 0 до 100")
            self.subjects[subject]['test_score'].append(test_score)

    def get_average_test_score(self, subject):
        if self.__getattr__(subject):
            test_scores = self.subjects[subject]["test_score"]
            return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        grades = []
        for subject in self.subjects.values():
            for grade in subject["grade"]:
                grades.append(grade)
        return sum(grades) / len(grades)


# # test 1
# student = Student("Иван Иванов", "subjects.csv")
# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)
# student.add_grade("История", 5)
# student.add_test_score("История", 92)
# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")
# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")
# print(student)
# """
# Ожидаемый ответ:
# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История
# """

# # test 2
# student = Student("123 Иван", "subjects.csv")
# '''
# Ожидаемый ответ:
# ValueError: ФИО должно состоять только из букв и начинаться с заглавной буквы
# '''

# # test 3
# student = Student("Петров Петр", "subjects.csv")
# student.add_grade("Физика", 6)
# '''
# Ожидаемый ответ:
# ValueError: Оценка должна быть целым числом от 2 до 5
# '''

# # test 4
# student = Student("Сидоров Сидор", "subjects.csv")
# average_history_score = student.get_average_test_score("Биология")
# '''
# Ожидаемый ответ:
# ValueError: Предмет Биология не найден
# '''
