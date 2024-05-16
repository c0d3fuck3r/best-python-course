# 1. Constants
# 2. Explain pythonic entrypoint
# 3. Explain while loop with examples
# 4. Explain conditional expressions
# 5. Explain Truthy/Falsy values
# 6. Explain input/print
# 7. Explain strings and their methods(what is .strip())

LOGIN = "admin"
PASSWORD = "qwerty"

if __name__ == "__main__":

    # alternate version of loop
    # login = ""
    # while not login:
    #     login = input("Enter login: ").strip()

    while True:
        login = input("Enter login: ").strip()
        if login:
            break

    while True:
        password = input("Enter pass: ").strip()
        if password:
            break

    # simple version
    if login == LOGIN and password == PASSWORD:
        print("Access granted")
    else:
        print("Access denied")
