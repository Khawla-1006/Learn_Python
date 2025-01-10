# Please write a program which asks the user for a string and then prints it out 
# so that exactly 20 characters are displayed. 
# If the input is shorter than 20 characters, 
# the beginning of the line is filled in with * characters.

# You may assume the input string is at most 20 characters long.
# Please type in a string: python
# **************python

# solution:
string_input = input("Please type in a string: ")
star = 20 - len(string_input)
print("*" * star + string_input)





# Part 2 : framed word 
# Word: testing

# ******************************
# *          testing           *
# ******************************

# string_input = input("Please type in a string: ")
# print("*" * 30)
# print("*" + string_input.center(28) + "*")
# print("*" * 30)


#without center()
word = input("word: ")
print("*" * 30)
spaces_at_start = (28-len(word)) // 2 
spaces_at_end = spaces_at_start

if len(word) % 2 != 0:
    spaces_at_end += 1 
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
print("*" * 30)