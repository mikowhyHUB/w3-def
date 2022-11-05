#Write a program in Python that asks the user to enter an integer n and display the multiplication table of that number.

def multi(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(i*j, end= '\t')
        print('\n')
        
n = int(input())
multi(n)