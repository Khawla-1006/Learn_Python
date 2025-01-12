number = int(input("Please type in a number: "))
i = 1 
while True :
    j = 1
    while j <= number :  
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
    if i == j :
        break 