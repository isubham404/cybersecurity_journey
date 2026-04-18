password = input("Enter your PassWord : ")

score = 0
feedback = []

#length check 

if len(password) >= 8: 
    score+=1
else :
    feedback.append("The password should be of 8 digits or more..") 

#UperCase check 
if any(char.isupper() for char in password):
    score+=1
else :
    feedback.append("The Password should contain a capital letter..")

#lowercase check 
if any(char.islower() for char in password):
    score+=1
else :
    feedback.append("The Password must contain a lower case letter..")

#Digits check 
if any(char.isdigit() for char in password):
    score+=1
else:
    feedback.append("The Password must contain a digit in it..")

#Symbol Check 
if any(char.isalnum() for char in password):
    score +=1
else:
    feedback.append("The Password should have a symbol in it..")

#Results 
if score == 5 :
    print("Strong Password ⚡ ")

elif score >= 3 :
    print("Medium Password 👍")

else :
    print("Weak PassWord !! ❌")


#Feedback Section
if feedback :
    print("Suggestion for stronger PassWord\n")
    for i in feedback:
        print("--> ",i)

