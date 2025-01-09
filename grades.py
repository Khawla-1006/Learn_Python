pt = int(input("How many points [0-100]: "))

# if pt >= 0 and pt <= 49 :
#     print("Grade : fail")
# elif pt >= 50 and pt <= 59 : 
#     print("Grade : 1")
# elif pt >= 60 and pt <= 69 : 
#     print("Grade : 2")
# elif pt >= 70 and pt <= 79 : 
#     print("Grade : 3")
# elif pt >= 80 and pt <= 89 : 
#     print("Grade : 4")
# elif pt >= 90 and pt <= 100 :
#     print("Grade : 5")
# else : 
#     print("Impossible!")

if pt < 0 or pt > 100 :
    grade = "impossible!"
elif pt < 50 :
    grade = "fail"
elif pt < 60 : 
    grade = "1"
elif pt < 70 : 
    grade = "2"
elif pt < 80 :
    grade = "3"
elif pt < 90 : 
    grade = "4"
else : 
    grade = "5"
print(f"Grade: {grade}")

