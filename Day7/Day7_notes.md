# Day 7 - Password Verification System Using Hashing

---

## Objective

To understand how hashing is used in real-world authentication systems and implement a basic password verification system using Python.

---

## Introduction

In real-world applications, passwords are never stored in plain text. Instead, systems store a hashed version of the password. During login, the entered password is hashed and compared with the stored hash.

This project demonstrates a simple implementation of that concept.

---

## Problem with Plain Text Passwords

If passwords are stored directly:

Example:
password123

Any unauthorized person can read or misuse it.

This creates a major security risk.

---

## Solution: Hashing

Instead of storing the password, we store its hash.

Example:
Input: password123
Stored: ef92b778bafe... (hashed value)

Even if someone accesses the database, they cannot easily retrieve the original password.

---

## Authentication Process

1. User registers with a password
2. System converts password into a hash
3. Hash is stored instead of actual password

During login:

1. User enters password
2. System hashes the entered password
3. Compares it with stored hash
4. If both match → access granted
5. If not → access denied

---

## Python Implementation

### Code

```python
import hashlib

stored_pass = "Subham@123"
hash_stored = hashlib.sha256(stored_pass.encode()).hexdigest()

user_pass = input("Enter the password for verification >> ")
user_hash = hashlib.sha256(user_pass.encode()).hexdigest()

if hash_stored == user_hash:
    print("User Verified!!")
else:
    print("Wrong Password ! Please try again")
```

---

## Code Explanation

### 1. Import Library

```python
import hashlib
```

The hashlib module is used to implement hashing algorithms like SHA-256.

---

### 2. Store Password

```python
stored_pass = "Subham@123"
```

This is the original password. In real systems, this is not stored directly.

---

### 3. Generate Stored Hash

```python
hash_stored = hashlib.sha256(stored_pass.encode()).hexdigest()
```

* encode() converts string into bytes
* sha256() applies hashing algorithm
* hexdigest() converts output into readable format

---

### 4. Take User Input

```python
user_pass = input("Enter the password for verification >> ")
```

User enters password for verification.

---

### 5. Hash User Input

```python
user_hash = hashlib.sha256(user_pass.encode()).hexdigest()
```

User input is converted into hash using the same method.

---

### 6. Compare Hashes

```python
if hash_stored == user_hash:
```

If both hashes match:

* Password is correct

Otherwise:

* Password is incorrect

---

## Important Concepts

### 1. Hashing

Converts input data into fixed-length output. It is not reversible.

---

### 2. SHA-256

A secure hashing algorithm widely used in cybersecurity.

---

### 3. Encoding

Converts string into byte format required for hashing.

---

### 4. Hexadecimal Output

Hash values are displayed in base-16 format for readability.

---

## Characteristics of Secure Password Handling

* Passwords should not be stored in plain text
* Only hashes should be stored
* Same hashing method must be used for comparison
* Even small input changes produce different hashes

---

## Limitations of This Program

* Password is hardcoded in the program
* Hash is generated each time program runs
* No database or file storage
* No multiple user support
* No retry or attempt limit

---

## Improvements Possible

* Store hash in a file or database
* Allow multiple users
* Add retry system
* Add password strength checking
* Use salting for better security

---

## Learning Outcome

* Understood how hashing is used in authentication
* Learned password verification logic
* Implemented SHA-256 hashing in Python
* Understood difference between plain text and hashed storage
* Built a basic authentication system

---

## Conclusion

This project demonstrates a fundamental concept used in real-world systems for secure authentication. It provides a strong foundation for understanding password security and prepares for more advanced cybersecurity topics.
