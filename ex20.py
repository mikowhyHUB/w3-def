def is_armstrong_number(number):
    final = number
    length = len(str(number))
    outcome = 0
    while number > 0:
        num = number % 10
        num = num ** length
        outcome += num
        number = number // 10

    if outcome == final:
        return True
    else:
        return False


print(is_armstrong_number(154))
