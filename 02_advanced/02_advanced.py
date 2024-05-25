# 1. Explain importing modules (Гэддис с.257-261)
#    https://www.youtube.com/watch?v=vqsalStEu38&list=PLlWXhlUMyooaeSj8L8tVVbtUo0WCO4ORR&index=17
# 2. Explain how to research library functions
#    ...
# 3. How to pass parameters. Take a note on types (Гэддис c.245-252)
#    https://www.youtube.com/watch?v=Zb3lF4qfElA&list=PLlWXhlUMyooaeSj8L8tVVbtUo0WCO4ORR&index=7
# 4. Brief note about what is ContextManager
#    https://www.youtube.com/watch?v=fUJT0TVfcFo&list=PLlWXhlUMyooaeSj8L8tVVbtUo0WCO4ORR&index=14
# 5. "open" function. What is file: descriptor, mode (Гэддис с.308-...)
# 6. TextIOWrapper API (Гэддис с.308-...)
# 7. Note on lists and destructuring (Про списки будет позже)
# 8. What is encoding/decoding ("some string".encode(), b"some bytes".decode())

# Задание сделать скрипт:
# 1. Создает пользователя:
# 1.1 Спрашивает логин и пароль.
# 1.2 Проверяет, что пароль не меньше 8 символов
#     И содержит буквы И цифры
# 1.3 Записывает логин и хэш пароля в файл.


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

    # open file with context manager
    with open("user.txt") as f:
        # long imperative way
        # line = f.readline().strip()
        # _login, _digest = line.split(" ")

        # short way
        # this is called "chaining" of "fluent interface"

        # read one line from file
        _login, _digest = f.readline().strip().split()

    # generate hash from input password
    digest = hashlib.sha256(password.encode()).hexdigest()

    # compare
    if login == _login and digest == _digest:
        print(f"Access granted for user {login}")
    else:
        print(f"Access denied for user {login}")
