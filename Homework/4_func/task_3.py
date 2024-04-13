'''
У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой,
выполняя следующие операции, для выполнения которых необходимо написать следующие функции:

check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

Пополнение счета:
Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.

Снятие средств:
Функция withdraw(amount) позволяет клиенту снимать средства со счета.
Сумма снятия также должна быть кратной MULTIPLICITY.
При снятии средств начисляется комиссия в процентах от снимаемой суммы,
которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:
Функция exit() завершает работу с банковским счетом.
Перед завершением, если на счету больше RICHNESS_SUM,
начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:
Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
Input:
deposit(10000)
withdraw(4000)
exit()

Print(operations)
Output:
 ['Пополнение карты на 10000 у.е. Итого 10000 у.е.', 'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']

'''
import decimal

MULTIPLICITY = 50  # Сумма снятия должна быть кратной этой переменной
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)  # процент за снятие
MIN_REMOVAL = decimal.Decimal(30)  # минимальное снятие
MAX_REMOVAL = decimal.Decimal(600)  # максимальное снятие
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)  # % депозита
COUNTER4PERCENTAGES = 3  # счетчик процента
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)  # налог на богатство
RICHNESS_SUM = decimal.Decimal(10_000_000)  # если на счету больше

bank_account = decimal.Decimal(0)  # банковский счет
count = 0  # сумма операции
operations = []  # Совершенные операции


def check_multiplicity(count):  # готово
    '''Проверка кратности суммы, кратна ли сумма amount заданному множителю MULTIPLICITY, при пополнении и снятии.'''
    if count % MULTIPLICITY == 0:
        return True
    return False


def check_multiplicity(amount):
    """Проверка кратности суммы при пополнении и снятии.
    Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY."""
    return True if amount % MULTIPLICITY == 0 else False


def deposit(amount):
    """Пополнение счёта. Функция позволяет клиенту пополнять свой счет на определенную сумму.
    Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY"""
    if check_multiplicity(amount):
        global bank_account
        bank_account += amount
        msg = f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.'
        operations.append(msg)
    else:
        msg = 'Сумма должна быть кратной 50 у.е.'
        print(msg)
    return msg


def withdraw(amount):
    """Снятие денег
    Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия также должна быть кратной
MULTIPLICITY. При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться
 от MIN_REMOVAL до MAX_REMOVAL"""
    commission = amount * PERCENT_REMOVAL
    if commission < MIN_REMOVAL:
        commission = MIN_REMOVAL
    elif commission > MAX_REMOVAL:
        commission = MAX_REMOVAL
    totaly_summ = amount + commission
    global bank_account
    if totaly_summ <= bank_account and check_multiplicity(amount):
        bank_account -= totaly_summ
        msg = f'Снятие с карты {amount} у.е. Процент за снятие {int(commission)} у.е.. Итого {int(bank_account)} у.е.'
        operations.append(msg)
    elif totaly_summ > bank_account and check_multiplicity(amount):
        msg = f'Недостаточно средств. Сумма с комиссией {int(totaly_summ)} у.е. На карте {bank_account} у.е.'
        operations.append(msg)
    else:
        msg = f'Недостаточно средств. Сумма с комиссией {int(totaly_summ)} у.е. На карте {bank_account} у.е.'
        operations.append(msg)
        msg = 'Сумма должна быть кратной 50 у.е.'
        print(msg)
    return msg


def exit():
    """Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях
    Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM,
начисляется налог на богатство в размере RICHNESS_PERCENT процентов"""
    global bank_account
    if bank_account > RICHNESS_SUM:
        rich_tax = bank_account * RICHNESS_PERCENT
        bank_account -= rich_tax
        msg = f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {rich_tax} у.е. Итого {bank_account} у.е.'
        operations.append(msg)
    msg = f'Возьмите карту на которой {(bank_account)} у.е.'
    operations.append(msg)
    return msg

deposit(1000)
withdraw(200)
exit()

print(operations)
