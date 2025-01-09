print("Please type in integer numbers. Type in 0 to finish.")
numbers_typed_in = 0
sum = 0 
positive = 0 
while True : 
    number = int(input("Number:"))
    if number == 0 :
        break
    if number > 0 :
        positive += 1 
    numbers_typed_in += 1
    sum += number
print(f"Numbers typed in {numbers_typed_in}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / numbers_typed_in}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {numbers_typed_in - positive}")