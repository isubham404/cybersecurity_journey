# 🔐 Encryption - Detailed Notes 

##  What is Encryption?

Encryption is the process of converting **readable data (plain text)** into an **unreadable format (cipher text)** so that unauthorized people cannot understand it.

👉 Only someone with the correct key or method can convert it back (decryption).

---

###  Simple Example:

* Plain Text: HELLO
* Encrypted Text: KHOOR

---

##  Important Terms

### 1️⃣ Plain Text

The original readable message
👉 Example: "password123"

---

### 2️⃣ Cipher Text

The encrypted (hidden) message
👉 Example: "sdvvzrug123"

---

### 3️⃣ Encryption

Process of converting plain text → cipher text

---

### 4️⃣ Decryption

Process of converting cipher text → plain text

---

### 5️⃣ Key

A secret value used to encrypt and decrypt data
👉 Example: shift = 3 in Caesar Cipher

---

##  Why is Encryption Important?

Encryption is used to protect sensitive information.

###  Uses:

* Protecting passwords
* Securing online banking
* Private messaging (WhatsApp, Signal)
* Secure websites (HTTPS)
* Data storage security

👉 Without encryption, anyone could read your personal data.

---

##  Types of Encryption

---

### 🔹 1. Symmetric Encryption

👉 Same key is used for encryption and decryption

* Fast
* Used in file encryption

 Example:

* AES (Advanced Encryption Standard)

---

### 🔹 2. Asymmetric Encryption

👉 Uses two keys:

* Public key (for encryption)

* Private key (for decryption)

* More secure

* Used in internet communication

 Example:

* RSA ( advanced Cryptography ) 

---

##  What is Caesar Cipher?

A simple encryption method where each letter is shifted by a fixed number.

---

###  Example (Shift = 3)

| Letter | Encrypted |
| ------ | --------- |
| A      | D         |
| B      | E         |
| C      | F         |

👉 HELLO → KHOOR

---

##  How Encryption Works (Basic Idea)

1. Take input (plain text)
2. Apply algorithm (rules)
3. Use a key
4. Generate cipher text

---

##  How We Use Encryption in Real Life

---

###  1. HTTPS (Secure Websites)

When you visit a secure website:

👉 Your data is encrypted before sending
👉 No one in between can read it

Example:

* Login credentials
* Credit card details

---

###  2. Messaging Apps

Apps like WhatsApp use:
👉 End-to-End Encryption

Meaning:

* Only sender and receiver can read messages
* Even the company cannot read them

---

###  3. Online Banking

* Transactions are encrypted
* Prevents hacking and data theft

---

###  4. Password Storage

Websites don’t store your actual password.

👉 They store a **hashed version** (encrypted form)

---

## 📌 Difference Between Encryption and Hashing

| Feature    | Encryption           | Hashing         |
| ---------- | -------------------- | --------------- |
| Reversible | Yes                  | No              |
| Purpose    | Secure communication | Store passwords |
| Example    | AES, RSA             | SHA-256         |

---

##  Limitations of Simple Encryption (Like Caesar Cipher)

* Easy to break 
* Not secure 
* Only used for learning

---

##  What I Learned

* Meaning of encryption
* Importance in cybersecurity
* Types of encryption
* Real-world applications
* Basic implementation using Caesar Cipher

---

## Conclusion

Encryption is one of the most important concepts in cybersecurity. It helps protect data, ensure privacy, and secure communication in the digital world.

Understanding basic encryption is the first step toward becoming a cybersecurity professional.
