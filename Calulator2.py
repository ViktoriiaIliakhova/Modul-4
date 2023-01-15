import logging
logging.basicConfig(level=logging.DEBUG)
operator = input("Введи дію, використовуючи відповідне число: 1 Додавання, 2 Віднімання, 3 Множення, 4 Ділення = ")
x = float(input("Введіть значення числа x = "))
y = float(input("Введіть значення числа y = "))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calc(operator, x, y):
    if operator == "1":
        logging.info(f"Додаю {x}, {y}")
        return add(x, y)

    elif operator == "2":
        logging.info(f"Від {x} віднімаю {y}")
        return subtract(x, y)

    elif operator == "3":
        logging.info(f"Множу {x} на {y}")
        return multiply(x, y)

    elif y != 0:
        if operator == "4":
            logging.info(f"Ділю {x} на {y}")
            return x / y

    elif y == 0:
        logging.info("Ділення на 0")
        return None

result = calc(operator, x, y)
print(result)
