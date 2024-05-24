# Count Vowels and Consonants: Write a function to count the number of vowels and consonants in a given string.

string = input("Enter the String: ").lower()

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

count_con = 0
count_vow = 0

for i in string:
    if i in consonants:
        count_con+=1
    else:
        count_vow+=1

print("""
Number of consonants: {}
Number of vowels: {}
""".format(count_vow, count_con))