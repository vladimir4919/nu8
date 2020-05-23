"""
Программа "Банковский счет"
Работа программы:
Запускаем программу.На счету -0
Программа предлагает:
1. пополнить счет
2. оплатить покупку
3. вывести историю покупок
4. выход
Добавлено сохранение суммы счета в файл.
При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохраняется история покупок
При следующем открытии программы прочитать сумму счета, которую сохранили
"""
import pickle
import os


def input_amount():  # функция ввода суммы
    """
    ОБРАБОТКА ИСКЛЮЧЕНИЙ
    """
    try:
        amount = float(input('Введите сумму:'))
    except:
        print('Сумма должна быть числом!')
        amount = 0
    else:
        if amount < 0:
            print('Отрицательные суммы не используются!')
        """
        ТЕРНАРНЫЙ ОПЕРАТОР
        """
        amount = amount if amount >= 0 else 0







FILE_NAME = 'history.data'
FILE_NAME1= 'account.data'
history = []
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'rb') as f:
        history = pickle.load(f)

def replenish_balance(account, history):#Функция пополнения баланса
    try:
        replenish_sum = float(input("\nВводим сумму пополнения счета: "))
    except:
        print('Сумма должна быть числом!')
        replenish_sum = 0
    else:
        if replenish_sum < 0:
            print('Отрицательные суммы не используются!')
            """
            ТЕРНАРНЫЙ ОПЕРАТОР
            """
            replenish_sum = replenish_sum if replenish_sum >= 0 else 0

    return account + replenish_sum, history
    print(account)

def purchase(account,history): #Функция  покупки

    """
       ОБРАБОТКА ИСКЛЮЧЕНИЙ
    """
    try:

        purchase_sum = float(input("\nВводим сумму покупки: "))

    except:
        print('Сумма должна быть числом!')
        purchase_sum = 0
    else:
        if  purchase_sum < 0:
            print('Отрицательные суммы не используются!')
            """
            ТЕРНАРНЫЙ ОПЕРАТОР
            """
            purchase_sum = purchase_sum if purchase_sum >= 0 else 0


    if account - purchase_sum >= 0:
        purchase_name = input("Вводим название покупки:")
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'rb') as f:
                history = pickle.load(f)
        history.append(f"Покупка \"{purchase_name}\" на сумму {purchase_sum}")

        print(f" На счету осталось {account-purchase_sum}")
    else:
        print("На счету недостаточно средств")
        return account, history
    return account-purchase_sum, history



def print_history(history): #Печать истории изменений баланса счета
    for elem_history in history:
        print(elem_history)
    return



def bank_account_run(account,history):

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню:')
        if choice == '1':
            account, history = replenish_balance(account, history)
            print('Состояние счета:', account)

        elif choice == '2':
            account, history = purchase(account, history)
        elif choice == '3':
            print_history(history)
        elif choice == '4':
            if os.path.exists(FILE_NAME1):
                with open(FILE_NAME1, 'wb') as f:
                    pickle.dump(account, f)
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, 'wb') as f:
                    pickle.dump(history, f)
            break
#if '_name_' == "_main_":
account = 0
history = []
bank_account_run(account,history)