"""
Define a function called reverse that takes a string textand returns that string in reverse.
For example: reverse("abcd") should return "dcba".
"""

def reverse(text):
    index = len(text) - 1
    new_string = ''
    for letter in range(len(text)):
        new_string += text[index]
        index -= 1
    return new_string
