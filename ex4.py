'''Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34'''


def fibinacci():

    prev = 0
    num = 1

    while num < 50:
        print(num)
        prev = num
        num = prev + num


fibinacci()
