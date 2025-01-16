while True : 
    number = int(input("Please type in a number: "))
    if number <= 0 :
        break
    i = 1
    fact = 1
    while i <= number :
        fact = fact * i
        i += 1
    print(f"The factorial of the number {number} is {fact}")    
print("Thanks goodbye!")