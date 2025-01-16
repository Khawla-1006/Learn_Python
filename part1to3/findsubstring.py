string = input("Please type in a word: ")
char = input("please type in a character: ")

# The program then prints the first three character slice
# which begins with the character specified by the user. 

# if char in string : 
#     index = string.find(char)
#     output = string[index : index + 3]
#     if len(output) == 3 :
#         print(output)   
i = 0
while True :
    if len(string) == 0 :
        break
    if char in string :
        index = string.find(char)
        output = string[index : index + 3]
        if len(output) == 3 : 
            print(output)
    i = index + 1
    string = string[i :]

# or simply

index = 0 

while index + 3 <= len(string) :
    if string[index] == char :
        print(string[index : index + 3])
    index += 1