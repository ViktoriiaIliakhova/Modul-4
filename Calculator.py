import logging

logging.basicConfig(level=logging.DEBUG)
operator = input("Введи дію, використовуючи відповідне число: 1 Додавання, 2 Віднімання, 3 Множення, 4 Ділення = ")
x = float(input("Введіть значення числа x = "))
y = float(input("Введіть значення числа y = "))
def calc(operator, x, y):
    if operator == "1":
        add_number = input("Бажаєте ввести ще одне число? [Т/Н]")
        if add_number == "Т":
            a = float(input("Введіть значення числа a = "))
            logging.info(f"Додаю {x}, {y} та {a}")
            return x + y + a
        elif add_number == "Н":
            logging.info(f"Додаю {x} {y}")
            return x + y
    elif operator == "2":
        logging.info(f"Від {x} віднімаю {y}")
        return x - y

    elif operator == "3":
        add_number = input("Бажаєте ввести ще одне число? [Т/Н]")
        if add_number == "Т":
            a = float(input("Введіть значення числа a = "))
            logging.info(f"Множу {x} на {y} та {a}")
            return x * y * a
        elif add_number == "Н":
            logging.info(f"Множу {x} на {y}")
            return x * y

    elif y != 0:
        if operator == "4":
            logging.info(f"Ділю {x} на {y}")
            return x / y

    elif y == 0:
        logging.info("Ділення на 0")

result = calc(operator, x, y)
print(result)