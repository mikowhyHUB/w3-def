print('Welcome to my Python quiz!')

playing = input('Do you want to play?\n')

if playing.lower() != 'yes':
    quit()
score = 0

answer = input('Question 1\nThe in operator is used to check if a value exists within an iterable object container such as a list. Evaluate to True if it finds a variable in the specified sequence and False otherwise.\nType true or false\n')
if answer.lower() == 'b':
    score += 1

answer = input('Question 2\nWhat is the output of the following code?\np, q, r = 10, 20 ,30\nprint(p, q, r)\na)10 20 30  b)10 20  c)Error:invalid syntax\nType a,b,c,\n')
if answer.lower() == 'a':
    score += 1

answer = input('Question 3\nWhich operator has higher precedence in the following list:\na)% (Modulus)  b)& (BitWise AND)  c)** (Exponent)  d)> (Comparison)Type a,b,c,d\n')
if answer.lower() == 'b':
    score += 1

answer = input(
    'Question 4\nWhat is the ouput of the following code?\nstr = \"pynative\"\nprint(str[1:3])\na)py  b)yn  c)pyn  d)yna\nType a,b,c,d\n')
if answer.lower() == 'b':
    score += 1

answer = input('Question 5\n Every time when we modify the string, Python Always create a new String and assign a new string to that variable.\nType true or false\n')
if answer.lower() == 'true':
    score += 1

answer = input(
    'Last question. This one is for 2 points!\nWhat is the Output of the following code?\n for x in range(0.5, 5.5, 0.5):\nprint(x)\na)[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]\nb)[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]\nc)The Program executed with errors\nType a,b,c\n')
if answer.lower() == 'c':
    score += 2

print('You got', score, 'questions correct!')
print('You got', (score/7)*100, '% correct answears!')
