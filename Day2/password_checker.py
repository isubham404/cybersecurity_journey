print("The Password should be of 8 digits and should contain Lower Case , Uper Case , numbers and symbols ")
password = input("Enter the password : ")

length = len(password)
has_uper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

if length>=8 and has_uper and has_lower and has_digit and has_symbol :
    print("Strong Password !! 💪 ")
elif length < 8 :
    print(" Enter 8 digits password !! ⚠️ ")
else:
    print("weak password ❌ ")
