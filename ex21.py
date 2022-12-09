def square_of_sum(number):
    outcome = 0
    for num in range(1, number+1):
        outcome += num
    return outcome ** 2


def sum_of_squares(number):
    outcome = 0
    for num in range(1, number+1):
        outcome += num ** 2
    return outcome


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


print(difference_of_squares(10))
