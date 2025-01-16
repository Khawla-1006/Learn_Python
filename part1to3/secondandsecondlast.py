string_input = input("Please type in a string: ")

if string_input[1] == string_input[-2] :
    print(f"The second and the second to last characters are {string_input[1]}")
else : 
    print("The second and the second to last characters are different")