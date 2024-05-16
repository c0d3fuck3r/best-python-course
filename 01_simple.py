# 1. Constants
# 2. Explain pythonic entrypoint
# 3. Explain while loop with examples
# 4. Explain conditional expressions
# 5. Explain Truthy/Falsy values
# 6. Explain input/print
# 7. Explain strings and their methods(what is .strip())

# Задание:
# 1. Написать скрипт
# 1.1 Спрашивать имя и возраст
# 1.2 Проверить что возраст больше 18ти(конвертация типов)
# 1.3 Если меньше, то ответить "Sorry ИМЯ. Access denied."
# 1.3 Если есть 18, то ответить "Hello ИМЯ. Access granted."

# 2. Написать скрипт
# 2.1 Сгенерировать случайное число в диапазоне от 0 до 9
#     (модуль random)
# 2.2 В бесконечном цикле просить угадать это число
#     (конвертация типов)
# 2.3 Если угадано, то выйти из цикла "Congratulations"
# 2.4 Если нет, то "You're wrong" и переспросить


LOGIN = "admin"
PASSWORD = "qwerty"

if __name__ == "__main__":

    # alternate version of loop
    # login = ""
    # while not login:
    #     login = input("Enter login: ").strip()

    # asking for login until it's not empty
    while True:
        login = input("Enter login: ").strip()
        if login:
            break

    # same for password
    while True:
        password = input("Enter pass: ").strip()
        if password:
            break

    # compare input with constant values
    if login == LOGIN and password == PASSWORD:
        print("Access granted")
    else:
        print("Access denied")
