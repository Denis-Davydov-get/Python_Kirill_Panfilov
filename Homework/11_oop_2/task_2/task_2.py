class Archive():
    _instance = None

    def __new__(cls, text: str, number: int):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        cls._instance.text = text
        cls._instance.number = number
        cls._instance.archive_text.append(text)
        cls._instance.archive_number.append(number)
        return cls._instance

    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f"Archive('{self.text}', {self.number})"

