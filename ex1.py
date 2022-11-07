'''Define a function that accepts a number and returns whether the number is even or odd.'''

def even_odd(num):
    if num % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')

while True:
    n = int(input('Type a number: '))
    even_odd(n)
   
    
