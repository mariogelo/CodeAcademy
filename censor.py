"""
Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.

For example:

censor("this hack is wack hack", "hack") 
should return

"this **** is wack ****"

"""

def censor(text, word): 
    if word in text: 
        return text.replace(word, "*" * len(word))
