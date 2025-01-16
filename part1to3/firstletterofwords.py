sentence = input("Please type in a sentence: ")
checker = " "
i = 0 
while i <= len(sentence) - 1 : 
    if i == 0 and sentence[0] != " "  :
        print(sentence[0])
    elif checker == sentence[i]:
        print(sentence[i + 1])
    i += 1
