PASSWORD = input("Введите пароль: ")


def is_very_long(PASSWORD):
    return len(PASSWORD) > 12


def has_digit(PASSWORD):
    return any(digit.isdigit() for digit in PASSWORD)


def has_upper_letters(PASSWORD):
    return any(letter.isalpha() and letter.isupper() for letter in PASSWORD)


def has_lower_letters(PASSWORD):
    return any(letter.isalpha() and letter.islower() for letter in PASSWORD)


def has_symbols(PASSWORD):
    return any(not letter.isdigit() and not letter.isalpha() for letter in PASSWORD)


def main(PASSWORD):
    score = 0

    checking_conditions = [
        is_very_long(PASSWORD),
        has_digit(PASSWORD),
        has_upper_letters(PASSWORD),
        has_lower_letters(PASSWORD),
        has_symbols(PASSWORD)
        ]

    for check in checking_conditions:
        if check:
            score += 2

    print("Рейтинг пароля: ", score)


if __name__ == '__main__':
    main(PASSWORD)
