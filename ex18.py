'''Write a Python program to print alphabet pattern 'E'. Go to the editor

'''
outcome = ''
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 0 or ((row == 0 or row == 6) and (column < 5 and column < 5) or (row == 3 and column < 4))):
            outcome += '*'
        else:
            outcome += ' '
    outcome += '\n'
print(outcome)
