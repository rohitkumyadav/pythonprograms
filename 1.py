# python program to revere the string

string = input("Enter the String: ")
#new_string = string[::-1]  --method 1

#new_string = "".join(reversed(string))  --method 2

new_string = ""   # --method 3
for  char in string:
    new_string = char + new_string

print("String After reverse: {}".format(new_string))