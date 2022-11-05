#Write a program in Python that asks the user to enter an integer n and display all the divisors of that number.

def divisors(num):
    div =[]
    for i in range(1,num+1):
        if num % i == 0:
            div.append(i)
    print(div)
    
x = int(input('num: '))
divisors(x)