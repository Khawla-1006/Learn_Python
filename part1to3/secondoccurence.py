string = input("Please type in a word: ")
sub = input("please type in a substring: ")

index = 0 
occurrence_index = []
while index + len(sub) <= len(string) :
    if string[index : index + len(sub)] == sub :
        occurrence_index.append(index)
        index = index + len(sub)
    else : 
        index += 1

if len(occurrence_index) >= 2 and occurrence_index[1] != -1 : 
    print("The second occurrence of the substring is at index ", occurrence_index[1]) 
else : 
    print("The substring does not occur twice in the string.")

    #YOU MUST BE PROUD OF THIS !! ITS YOUR OWN SOLUTION AFTER 8 HOURS STRAIGHT :)