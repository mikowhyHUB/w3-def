'''Define a function that accepts lowercase words and returns uppercase words.'''

def lower_to_upper(lowercase):
    uppercase = lowercase.upper()
    return uppercase

words = input()
print(lower_to_upper(words))