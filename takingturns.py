# Please write a program which asks the user to type in a number.
# The program then prints out the positive integers between 1 and the number itself,
# alternating between the two ends of the range

number = int(input("Please type in a number:"))


i = 1
j = number

while j >= i :
    if j != i : 
        print(i)
    print(j)
    i += 1 
    j -= 1
