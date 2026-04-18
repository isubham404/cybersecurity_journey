password = input("Enter your PassWord : ")

score = 0

#length check 

if len(password) >= 8: 
    score+=1 

#UperCase check 
if any(char.isupper() for char in password):
    score+=1

#lowercase check 
if any(char.islower() for char in password):
    score+=1

#Digits check 
if any(char.isdigit() for char in password):
    score+=1

#Symbol Check 
if any(char.isalnum() for char in password):
    score +=1

if score == 5 :
    print("Strong Password ⚡ ")

elif score >= 3 :
    print("Medium Password 👍")

else :
    print("Weak PassWord !! ❌")

