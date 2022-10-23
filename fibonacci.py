'''
Display Fibonacci series up to 10 terms
'''
num1 = 1
num2 = 0
for i in range(10):
    print(num2, end=' ')
    result = num1 + num2
    num1 = num2
    num2 = result
