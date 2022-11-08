'''Define a function that returns Factorial of a number.'''

def factorial(num):
    outcome = 1
    for i in range(num+1):
        outcome*=num
        print(outcome)

factorial(6)
