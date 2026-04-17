import hashlib 
users = {"subham": hashlib.sha256("Subham@123".encode()).hexdigest()
         ,"admin": hashlib.sha256("admin@123".encode()).hexdigest()
         ,"sarthak" : hashlib.sha256("sarThak12@2006".encode()).hexdigest()
         }

while True:
    userName = input("Enter the user name : ")
    passWord = input("Enter your password : ")
    if userName in users :
        hashed_input =  hashlib.sha256(passWord.encode()).hexdigest()
    
        if users[userName] == hashed_input:
            print("Login Successfull !!")
            break
        else:
            print("Incorrect Password !! Try Again !!\n")
    else :
        print("User Not found !! Try Again!!\n")
