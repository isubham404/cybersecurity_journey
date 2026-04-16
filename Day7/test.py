import hashlib

# Step 1: Store password (hashed)
stored_password = "Subham@123"

stored_hash = hashlib.sha256(stored_password.encode()).hexdigest()

# Step 2: User input
user_input = input("Enter password: ")

# Step 3: Hash user input
user_hash = hashlib.sha256(user_input.encode()).hexdigest()

# Step 4: Compare
if user_hash == stored_hash:
    print("Access Granted")
else:
    print("Access Denied")