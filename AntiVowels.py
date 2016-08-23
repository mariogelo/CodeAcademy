"""
Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
------------------------------------

def anti_vowel(text):
    vowels="aeiouAEIOU"
    word = ''
    for letter in text:
        if letter not in vowels:
            word += letter
    return word"""
    
def anti_vowel(text):
    for letter in text:
        if letter in "aeiouAEIOU":
            text = text.replace(letter,"")
    return text
