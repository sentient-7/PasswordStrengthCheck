import re   

print("*-----Password Strength Checker-----*\n\n")
print("12 characters minimum.\n")

def user_input():
    print("Enter the password:")
    password=str(input())
    return password

while True:
    password_1=user_input()
    if(len(password_1)<12):
        print("The password must be of 12 characters.")
    
    else:
        break



mediumStrength=re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).+$",password_1)
highStrength=re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*(\W)+).+$",password_1)

if highStrength:
    print("Password strength:Strong.")

elif mediumStrength:
    print("Password strength:Medium.")

else:
    print("Password Strength:Weak.")
    
    if((re.search(r"[A-Z]+",password_1)==None)):
       print("Missing Uppercase characters.")
    
    if((re.search(r"[0-9]+",password_1)==None)):
       print("Missing numbers.")         

    
    if((re.search(r"[a-z]+",password_1)==None)):
       print("Missing lowercase characters.")

    if((re.search(r"\W+",password_1))==None):
        print("Missing Symbols.")