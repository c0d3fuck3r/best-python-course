# 1. Explain importing modules
# 2. Explain how to research library functions
# 3. How to pass parameters. Take a note on types
# 4. Brief note about what is ContextManager
# 5. "open" function. What is file: descriptor, mode
# 6. TextIOWrapper API
# 7. Note on lists and destructuring
# 8. What is encoding/decoding

# Задание сделать скрипт:
# 1. Создает пользователя:
# 1.1 Спрашивает логин и пароль.
# 1.2 Проверяет, что пароль не меньше 8 символов
#     И содержит буквы И цифры
# 1.3 Записывает логин и хэш пароля в файл.
# 1.4 Если в файле уже есть запись, то добавляет новую.


from getpass import getpass
import hashlib


if __name__ == "__main__":

    while True:
        login = input("Enter login: ").strip()
        if login:
            break

    while True:
        password = getpass(prompt="Enter pass: ").strip()
        if password:
            break

    with open("user.txt") as f:
        # long imperative way
        # line = f.readline().strip()
        # _login, _digest = line.split(" ")

        # short way
        # this is called "chaining" of "fluent interface"
        _login, _digest = f.readline().strip().split()

    digest = hashlib.sha256(password.encode()).hexdigest()

    if login == _login and digest == _digest:
        print(f"Access granted for user {login}")
    else:
        print(f"Access denied for user {login}")
