# Day 6 - Hashing and SHA-256 Implementation

---

## Objective

To understand the concept of hashing and implement a basic hash generator using Python's hashlib library.

---

## What is Hashing?

Hashing is the process of converting input data (plain text) into a fixed-length string of characters, known as a hash value or digest.

The output generated is unique for each input and cannot be reversed to obtain the original data.

---

## Key Characteristics of Hashing

1. One-Way Function
   Hashing is not reversible. It is not possible to retrieve the original input from the hash value.

2. Fixed-Length Output
   Regardless of the input size, the output hash has a fixed length.

3. Deterministic
   The same input will always produce the same hash.

4. Avalanche Effect
   A small change in input produces a completely different hash output.

---

## Example

Input: hello
SHA-256 Hash: 2cf24dba5fb0a... (truncated)

Input: hello1
SHA-256 Hash: completely different value

---

## Common Hashing Algorithms

* MD5 (not secure for modern use)
* SHA-1 (deprecated)
* SHA-256 (widely used and secure)

---

## Applications of Hashing

1. Password Storage
   Passwords are stored as hashes instead of plain text.

2. Data Integrity
   Used to verify that data has not been altered.

3. Digital Signatures
   Ensures authenticity of data.

4. File Verification
   Used to check if files are modified or corrupted.

---

## Python Implementation

### Code

```python
import hashlib

text = input("Enter text: ")

hash_object = hashlib.sha256(text.encode())
hash_value = hash_object.hexdigest()

print("SHA-256 Hash:", hash_value)
```

---

## Code Explanation

### 1. Import Library

```python
import hashlib
```

The hashlib module provides functions to implement various hashing algorithms.

---

### 2. Take User Input

```python
text = input("Enter text: ")
```

Accepts input from the user.

---

### 3. Convert String to Bytes

```python
text.encode()
```

Hashing functions require input in byte format, so the string is encoded.

---

### 4. Create Hash Object

```python
hash_object = hashlib.sha256(text.encode())
```

This applies the SHA-256 hashing algorithm to the input data.

---

### 5. Generate Hash Value

```python
hash_value = hash_object.hexdigest()
```

Converts the hash into a readable hexadecimal format.

---

### 6. Display Output

```python
print("SHA-256 Hash:", hash_value)
```

Prints the generated hash.

---

## Important Terms

| Term        | Meaning                                      |
| ----------- | -------------------------------------------- |
| Hash        | Output generated from input data             |
| Digest      | Another name for hash                        |
| Algorithm   | Method used to generate hash (e.g., SHA-256) |
| Encoding    | Converting data into byte format             |
| Hexadecimal | Base-16 representation of data               |

---

## Limitations

* Hashing is not reversible
* Cannot retrieve original data from hash
* If two inputs produce same hash (rare), it is called a collision

---

## Learning Outcome

* Understood the concept of hashing
* Learned properties of hash functions
* Implemented SHA-256 hashing in Python
* Understood real-world applications of hashing

---

## Conclusion

Hashing is a fundamental concept in cybersecurity used for securing sensitive data such as passwords and ensuring data integrity. Understanding hashing is essential for building secure systems.
