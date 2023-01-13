import logging
logging.basicConfig(level=logging.DEBUG)
c = input("Введи дію, використовуючи відповідне число: 1 Додавання, 2 Віднімання, 3 Множення, 4 Ділення = ")
x = float(input("Введіть значення числа x = "))
y = float(input("Введіть значення числа y = "))
r = "result"
if c == "1":
    add_number = input("Бажаєте ввести ще одне число? [Т/Н]")
    if add_number == "Т":
        a = float(input("Введіть значення числа a = "))
        logging.info(f"Додаю {x}, {y} та {a}")
        r = x + y + a
    elif add_number == "Н":
        r = x + y
        logging.info(f"Додаю {x} {y}")

elif c == "2":
    r = x - y
    logging.info(f"Від {x} віднімаю {y}")

elif c == "3":
    add_number = input("Бажаєте ввести ще одне число? [Т/Н]")
    if add_number == "Т":
        a = float(input("Введіть значення числа a = "))
        r = x * y * a
        logging.info(f"Множу {x} на {y} та {a}")
    elif add_number == "Н":
        r = x * y
        logging.info(f"Множу {x} на {y}")

elif y != 0:
    if c == "4":
        r = x / y
        logging.info(f"Ділю {x} на {y}")

elif y == 0:
    logging.info("Ділення на 0")

print("Результат", r)

