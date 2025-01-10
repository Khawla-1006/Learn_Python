underline = ""

while True : 
    string_input = input("Please type in a string: ")
    if string_input == "" : 
        break
    else : 
        underline = "-" * len(string_input)
        print(string_input)
        print(underline)