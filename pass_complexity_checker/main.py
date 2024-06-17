
def seprator(passw):    
    userPass = []
    x = passw
    for i in x:
        userPass.append(i)
    return userPass


def length(data):
    userData = data
    if len(userData) > 8:
        print("\nLength of Password > 8 ✅")
        return 1
    else:
        print("\nLength of Password > 8 ❌")
        return 0

def specialchar(data):
    special = 0
    special_char = ['!','@','#','$','%','^','&','*']
    userData = data
    for i in userData:
        for j in special_char:
            if i == j:
                special = 1
    if special == 1:
        print("\nUse of Special Characters ✅ ")
        return 1
    else:
        print("\nUse of Special Character ❌")
        return 0       
            
def cases(userInput):
    lower = 0
    upper = 0
    digit = 0
    userData = userInput
    for i in range(0,len(userData)):
        if userData[i].islower():
            lower = 1
        if userData[i].isupper():
            upper = 1
        if userData[i].isdigit():
            digit = 1
    if lower == 1:
        print("\nUse of lowercase Characters ✅ ")
    else:
        print("\nUse of lowercase Characters ❌")
    if upper == 1:
        print("\nUse of uppercase Characters ✅ ")
    else:
        print("\nUse of uppercase Characters ❌")

    if digit == 1:
        print("\nUse of Numbers ✅ ")
    else:
        print("\nUse of Numbers ❌")

    return lower , upper , digit


userInput = input("\nPlease Enter the Password : ")
data = seprator(userInput)
length_check = length(data)
specialChar_check = specialchar(data)
alphaCases = cases(userInput)
lower,upper,digit = alphaCases

if length_check and specialChar_check and lower and upper and digit == 1:
    print(f"\n{userInput} is a Strong Password\n")
elif length_check and specialchar and (lower or upper or digit) == 1:
    print(f"\n{userInput} is a Moderate Password\n")
else:
    print(f"\n{userInput} is a Weak Password\n")