# 1. Explain dict
# 1.1 Explain KeyError
# 1.2 Show .get() method

# 2. Show ways to get only unique values
# 2.1 With list
# 2.2 With set(explain what is set)
# 2.3 Explain list comprehensions

# Задача
# Есть файл с логами.
# Достать из логов IP адреса
# Посчтитать IP адреса
# Вывести summary в конце

from pprint import pprint


if __name__ == "__main__":

    table = {}

    with open("duplicates.txt") as file:
        for name in file.readlines():

            name = name.strip().lower()

            if name in table:
                table[name] += 1
            else:
                table[name] = 1

    pprint(table, width=10)

    # unique using list
    names = []

    with open("duplicates.txt") as file:
        for name in file.readlines():

            name = name.strip().lower()

            if name not in names:
                names.append(name)

    print(names)

    # unique using hack
    with open("duplicates.txt") as file:
        names = [name.strip().lower() for name in names]
        names = list(set(names))

    print(names)
