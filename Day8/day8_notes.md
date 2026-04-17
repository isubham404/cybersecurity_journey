# Day 8 - Multi-User Authentication System Using Hashing

---

## Objective

To build a basic authentication system that supports multiple users and verifies login credentials using hashing.

---

## Introduction

In real-world applications, systems handle multiple users instead of a single user. Each user has a unique username and password. Passwords are stored securely using hashing.

This project demonstrates how to implement a simple multi-user authentication system using Python.

---

## Concept

Instead of storing plain text passwords, the system stores hashed passwords.

Each user is identified by:

* Username
* Hashed password

During login:

1. User enters username and password
2. System checks if the username exists
3. Password is hashed
4. Hash is compared with stored hash
5. If matched → login successful
6. If not → access denied

---

## Data Structure Used

A dictionary is used to store user data.

Example:

```python id="9bd0fa"
users = {
    "username1": "hashed_password1",
    "username2": "hashed_password2"
}
```

* Key → Username
* Value → Hashed password

---

## Python Implementation

### Code

```python id="e9xvcm"
import hashlib 

users = {
    "subham": hashlib.sha256("Subham@123".encode()).hexdigest(),
    "admin": hashlib.sha256("admin@123".encode()).hexdigest(),
    "sarthak": hashlib.sha256("sarThak12@2006".encode()).hexdigest()
}

while True:
    userName = input("Enter the user name: ")
    passWord = input("Enter your password: ")

    if userName in users:
        hashed_input = hashlib.sha256(passWord.encode()).hexdigest()

        if users[userName] == hashed_input:
            print("Login Successful!!")
            break
        else:
            print("Incorrect Password!! Try again.")
    else:
        print("User Not Found!! Try again.")
```

---

## Code Explanation

### 1. Import Library

```python id="bn69hw"
import hashlib
```

Used to perform hashing operations.

---

### 2. Store Users

```python id="g8t3hm"
users = { ... }
```

A dictionary stores usernames and their corresponding hashed passwords.

---

### 3. Infinite Loop

```python id="t3d4xr"
while True:
```

Allows repeated attempts until correct login.

---

### 4. Take Input

```python id="m2x7vn"
userName = input(...)
passWord = input(...)
```

User enters credentials.

---

### 5. Check Username

```python id="a1o0gk"
if userName in users:
```

Verifies if the user exists in the system.

---

### 6. Hash Password

```python id="8tnru2"
hashed_input = hashlib.sha256(passWord.encode()).hexdigest()
```

Converts user input password into hash.

---

### 7. Compare Hashes

```python id="jbz4gq"
if users[userName] == hashed_input:
```

If hashes match:

* Correct password

Else:

* Incorrect password

---

### 8. Break Statement

```python id="s3avc7"
break
```

Stops loop when login is successful.

---

## Key Concepts

### 1. Authentication

Process of verifying user identity using credentials.

---

### 2. Hashing

Converts password into secure format before storage.

---

### 3. Dictionary

Used to store and manage multiple users efficiently.

---

### 4. Loop Control

Allows repeated attempts for login.

---

## Program Features

* Supports multiple users
* Uses hashing for security
* Allows retry on failure
* Simple and easy to understand

---

## Limitations

* Users are hardcoded in the program
* No database or file storage
* No limit on login attempts
* No password masking
* No encryption for data transmission

---

## Possible Improvements

* Store users in a file or database
* Add limit to login attempts
* Implement password strength checking
* Add user registration feature
* Use salting for stronger security

---

## Learning Outcome

* Learned how multi-user systems work
* Understood authentication flow
* Practiced dictionary usage
* Applied hashing in real scenario
* Built a more realistic login system

---

## Conclusion

This project demonstrates how authentication systems handle multiple users securely using hashing. It provides a strong foundation for building more advanced and secure systems in cybersecurity.
