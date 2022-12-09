def square_of_sum(number):
    '''
    :param number: int - the number to square sum of
    :return: int - the sum of squares
    '''
    outcome = 0
    for num in range(1, number+1):
        outcome += num
    return outcome ** 2


def sum_of_squares(number):
    '''
    :param number: int - the number to square then add
    :return: int - the sum of numbers, first squared then added
    '''
    outcome = 0
    for num in range(1, number+1):
        outcome += num ** 2
    return outcome


def difference_of_squares(number):
    '''
    :param number: int - the number to square in both previous functions
    :return: int - the resoult of subtract of both functions
    '''
    return square_of_sum(number) - sum_of_squares(number)


print(difference_of_squares(10))
