current_year = int(input("Year:"))
attempts = 1
leap_year = 0
next_leap_year = 0
no_leap_year = current_year
while True : 
    if current_year % 100 == 0 and current_year % 400 == 0 :
            leap_year = current_year
            break
    elif current_year % 4 == 0 :
            leap_year = current_year
            break
    else : 
        current_year += 1
        attempts += 1

if attempts == 1 :
    next_leap_year = leap_year + 4
    print(f"The next leap year after {current_year} is {next_leap_year}")
else :
    print(f"The next leaped year after {no_leap_year} is {leap_year}")
