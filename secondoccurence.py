string = input("Please type in a word: ")
sub = input("please type in a substring: ")

index = 0 
occurrence_index = []
while index + len(sub) <= len(string) :
    if string[index : index + len(sub)] == sub :
        occurrence_index.append(index)
    index += 1

if len(occurrence_index) >= 2 and occurrence_index[1] != -1 : 
    print("The second occurrence of the substring is at index ", occurrence_index[1]) 
else : 
    print("The substring does not occur twice in the string.")