def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(digit.isdigit() for digit in password)


def has_upper_letters(password):
    return any(letter.isalpha() and letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.isalpha() and letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)


def main(password):
    score = 0

    checking_conditions = [
        is_very_long(password),
        has_digit(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password)
    ]

    for check in checking_conditions:
        if check:
            score += 2

    print("Рейтинг пароля: ", score)


if __name__ == "__main__":
    password = input("Введите пароль: ")
    main(password)
