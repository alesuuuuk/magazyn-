# Словник з цінами на товари
products = {
    'яблука': 10,
    'банани': 15,
    'апельсини': 12,
    'груші': 8,
    'киві': 20
}

# Початковий баланс покупця
balance = 100

# Покупки користувача
shopping_cart = []

flag = True

if __name__ == "__main__":
    while flag == True:
        print(products)
        product = input("Введіть індекс товару, якщо хочете вийти - напишітьт q ")
        if product == "1":
            if balance - 10 >= 0:
                shopping_cart.append("яблуко")
                balance -= 10
                print("Ваш кошик: ", shopping_cart, ", баланс --- ", balance)
            else:
                print("У вас недостатньо коштів, щоб купити цей товар")
        elif product == "2":
            if balance - 15 >= 0:
                shopping_cart.append("банан")
                balance -= 15
                print("Ваш кошик: ", shopping_cart, ", баланс --- ", balance)
            else:
                print("У вас недостатньо коштів, щоб купити цей товар")
        elif product == "3":
            if balance - 12 >= 0:
                shopping_cart.append("апельсин")
                balance -= 12
                print("Ваш кошик: ", shopping_cart, ", баланс --- ", balance)
            else:
                print("У вас недостатньо коштів, щоб купити цей товар")
        elif product == "4":
            if balance - 8 >= 0:
                shopping_cart.append("груші")
                balance -= 8
                print("Ваш кошик: ", shopping_cart, ", баланс --- ", balance)
            else:
                print("У вас недостатньо коштів, щоб купити цей товар")

        elif product == "5":
            if balance - 20 >= 0:
                shopping_cart.append("киві")
                balance -= 20
                print("Ваш кошик: ", shopping_cart, ", баланс --- ", balance)
            else:
                print("У вас недостатньо коштів, щоб купити цей товар")

        elif product == "q":
            flag = False
        else:
            print("товар не знайдено")




