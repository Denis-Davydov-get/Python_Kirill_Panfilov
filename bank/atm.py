# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

class atm:

    balance = None

    def add_balance(self, balance, summ_add):  # пополнить баланс
        if summ_add % 50:
            balance += summ_add
            return balance
        else:
            return 'Ошибка. Сумма пополнения должна быть кратна 50'


    def take_off(self, summ_general, summ_take_off): # снять с баланса
        if summ_take_off % 50 & summ_take_off >= summ_general:
            summ_general -= summ_take_off
            return summ_general


    def exit(self, summ_general): # посмотреть баланс
        return summ_general


    summ = 0
    while True:
        action = int(input('Что вы хотите сделать?: \n'
                       '1 - выйти.\n'
                       '2 - пополнить баланс.\n'
                       '3 - снять деньги.\n'))
        if action == 1:
            print(exit(summ))
        elif action == 2:
            summ_add = int(input("На какую сумму пополнить?"))
            print(add_balance(summ, summ_add))
        elif action == 3:
            summ_take_off = float("Какую суммы вы хотитите снять?")
            print(take_off(summ, summ_take_off))
