# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# Solution 1 - Using for loop
user_input1 = input('Enter a string: ')
new_str1 = ''
for char in user_input1:
    new_str1 += char * 2
print(new_str1)

#Solution 2 - Not using for loop
user_input2 = input("Enter a string: ")
new_str2 = ''.join(map(lambda char: char * 2, user_input2))
print(new_str2)




# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


# Solution
alphabet = "abcdefghijklmnopqrstuvwxyz"
user_range = input("Enter a range of letters (e.g., a-z): ")
start, end = user_range.split('-')

# Find the index of each letter
start_ind = alphabet.index(start.lower())
end_ind = alphabet.index(end.lower())

result = alphabet[start_ind:end_ind + 1]
# Return capital letters if the range was given in capital letters
result = ''.join(result).upper() if user_range.isupper() else ''.join(result)
print(result)