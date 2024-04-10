from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        return super().__new__(cls, value)

    def __init__(self, value, author):
        super().__init__()
        self.value = value
        self.author = author
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M')

    def __str__(self):
        return (f'{self.value} (Автор: {self.author}, Время создания: {self.time})')

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"


my_string = MyStr("Другой текст", "Бунин")
print(my_string)