# Python Program to check if the given text is palindrome or not

"""
a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam
"""

def palidrome(text):
    if text == text[::-1]:
        return "It is Palindrome"
    else:
        return "It is not Palindrome"
    

text = input("Enter the text: ")
#print(palidrome(text))


