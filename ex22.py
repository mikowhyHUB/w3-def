def square(number):

    if number == 1 or number == 2:
        return number
    elif number > 2 and number < 65:
        for num in range(2, number):
            grains = 2**num
        print(grains)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    for num in range(2, 65):
        outcome = 2 ** num
    print(outcome - 1)


total()
square(64)
