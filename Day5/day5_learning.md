# Day 5 - Caesar Cipher Tool (Encryption and Decryption)

---

## Objective

To understand the concept of encryption and decryption and implement a basic Caesar Cipher tool in Python that can perform both operations.

---

## Concepts Covered

### 1. Encryption

Encryption is the process of converting readable data (plain text) into an unreadable format (cipher text) using a specific method or key.

Example:
Plain Text: HELLO
Encrypted Text: KHOOR

---

### 2. Decryption

Decryption is the reverse process of encryption. It converts the encrypted data (cipher text) back into its original readable form (plain text).

Example:
Cipher Text: KHOOR
Decrypted Text: HELLO

---

### 3. Caesar Cipher

Caesar Cipher is a simple encryption technique where each letter in the text is shifted by a fixed number of positions.

Example with shift = 3:

| Letter | Encrypted |
| ------ | --------- |
| A      | D         |
| B      | E         |
| C      | F         |

---

## Logic Used in the Program

### Step 1: Take Input

The user enters the text that needs to be processed.

---

### Step 2: Choose Operation

The user selects:

* 'e' for encryption
* 'd' for decryption

---

### Step 3: Process Each Character

A loop is used to go through each character in the input text.

---

### Step 4: Check Character Type

Only alphabetic characters are processed using:
isalpha()

Non-alphabetic characters (spaces, numbers, symbols) remain unchanged.

---

### Step 5: Apply Shift Logic

* For encryption: shift forward (+ shift)
* For decryption: shift backward (- shift)

This is done using:

* ord() to convert character to ASCII value
* chr() to convert ASCII value back to character

---

### Step 6: Store Result

Each processed character is added to a result string.

---

### Step 7: Display Output

The final result (encrypted or decrypted text) is printed.

---

## Functions and Methods Used

| Function  | Purpose                          |
| --------- | -------------------------------- |
| input()   | Take user input                  |
| for loop  | Iterate through each character   |
| isalpha() | Check if character is a letter   |
| ord()     | Convert character to ASCII value |
| chr()     | Convert ASCII value to character |

---

## Program Features

* Supports both encryption and decryption
* Handles user input
* Ignores non-alphabetic characters
* Simple and easy to understand logic

---

## Limitations

* Does not handle wrap-around (Z to A)
* Works only for basic understanding
* Not secure for real-world applications

---

## Learning Outcome

* Understood encryption and decryption concepts
* Learned how Caesar Cipher works
* Practiced loops and conditional statements
* Used built-in functions like ord() and chr()
* Built a simple interactive Python tool

---

## Conclusion

This project demonstrates a basic implementation of encryption and decryption using the Caesar Cipher. It helps in understanding how simple encryption techniques work and builds a foundation for more advanced cryptographic concepts.
