'''
Write a program to use for loop to print the following reverse number pattern
'''

for i in range(5, 0, -1):
    for j in range(i):
        print(i-j, end=' ')
    print('\n')
