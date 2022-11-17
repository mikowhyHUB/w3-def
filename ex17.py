'''Write a Python program to print alphabet pattern 'D'''

result = ''
for row in range(0, 7):
    for column in range(0, 7):
        if (((column == 1 or column == 5) and row != 6 and row != 0) or ((row == 0 or row == 6) and (column > 0 and column < 5))):
            result = result + '*'
        else:
            result += ' '
    result += '\n'
print(result)
