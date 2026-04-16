import hashlib
stored_pass = "Subham@123"
hash_stored = hashlib.sha256(stored_pass.encode()).hexdigest()

while True:
    user_pass = input("Enter the password for verification >> ")
    user_hash = hashlib.sha256(user_pass.encode()).hexdigest()

    if user_hash == hash_stored:
        print("User Verified!!")
        break
    else:
        print("Wrong Password ! Please try again..")
