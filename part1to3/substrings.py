# Please write a program which asks the user to input a string. 
# The program then prints out different messages 
# if the string contains any of the vowels a, e or o.

string = input("Please type ina string: ")
vowels = "aeo"
index = 0 

while index < len(vowels) : 
    vowel = vowels[index]
    if vowel in string : 
        print(vowel,"found")
    else : 
        print(vowel,"not found")
    index += 1 