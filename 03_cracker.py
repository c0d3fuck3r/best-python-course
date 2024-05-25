# 1. Explain function:
# 1.1 Abstraction
# 1.2 Signature
# 1.3 Arguments binding to local vars
# 1.4 Clean functions and side effects
# 1.5 Type hints

# 2. Explain lists and some methods
# 2.1 Explain mutable and immutable methods difference

# 3. Explain for loops
# 3.1 Explain break, continue, pass

# 4. Explain boolean flag concept

# Задача
# Пропинговать список IP адресов
# По одному пакету на адрес
# summary

LOGIN = "admin"
PASSWORD = "qwerty"


# def is_valid(username: str, secret: str) -> bool:
#     return username == LOGIN and secret == PASSWORD


if __name__ == "__main__":

    passwords = []

    with open("passwords.txt") as f:

        # read file line by line and fill passwords list
        for password in f.readlines():
            passwords.append(password.strip())

    login = input("Enter login: ").strip()

    # flag that helps to indicate if credentials matched
    matched = False

    # loop through passwords and compare with input
    for password in passwords:
        if login == LOGIN and password == PASSWORD:
            matched = True
            print(f"Login and password matched: {login} {password}")
            break

    if not matched:
        print("No matching passwords")
