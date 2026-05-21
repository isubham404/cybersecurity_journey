# 🔐 Password Hashing & Cracking Lab

> A hands-on cybersecurity lab focused on understanding password hashing, hash generation, and cracking techniques using John the Ripper.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Objectives](#-objectives)
* [Tools Used](#-tools-used)
* [Lab Setup](#-lab-setup)
* [Hashing Concepts](#-hashing-concepts)
* [Generating Hashes](#-generating-hashes)
* [Password Cracking](#-password-cracking)
* [Attack Types](#-attack-types)
* [Common Errors & Fixes](#-common-errors--fixes)
* [Security Insights](#-security-insights)
* [Future Scope](#-future-scope)
* [Conclusion](#-conclusion)

---

## 📖 Overview

This lab demonstrates how passwords are converted into hashes and how attackers attempt to crack them using various techniques.

It provides practical exposure to:

* Hashing algorithms
* Password cracking tools
* Real-world attack strategies

---

## 🎯 Objectives

* Understand password hashing
* Generate hashes using multiple methods
* Crack hashes using John the Ripper
* Learn dictionary, brute-force, and hybrid attacks
* Understand limitations of hash cracking

---

## 🛠️ Tools Used

* John the Ripper
* RockYou Wordlist
* Python (hash generation)
* Linux/Kali Terminal

---

## ⚙️ Lab Setup

### Install John the Ripper

```bash
sudo apt update
sudo apt install john -y
```

### Setup Wordlist

```bash
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
```

---

## 🧠 Hashing Concepts

### What is Hashing?

Hashing is the process of converting input data into a fixed-length string using a mathematical algorithm.

```text
Input:  password
MD5:    5f4dcc3b5aa765d61d8327deb882cf99
```

---

### Properties of Hashing

* One-way function
* Deterministic output
* Avalanche effect (small change → big difference)

---

### Common Algorithms

| Algorithm | Status       | Usage            |
| --------- | ------------ | ---------------- |
| MD5       | ❌ Weak       | Legacy systems   |
| SHA1      | ❌ Weak       | Deprecated       |
| SHA256    | ✅ Moderate   | General use      |
| bcrypt    | 🔥 Strong    | Password storage |
| Argon2    | 🔥 Strongest | Modern security  |

---

## ⚙️ Generating Hashes

### Using Terminal

```bash
echo -n "password" | md5sum
echo -n "password" | sha1sum
echo -n "password" | sha256sum
```

---

### Using Python

```python
import hashlib

text = "password"

print("MD5:", hashlib.md5(text.encode()).hexdigest())
print("SHA1:", hashlib.sha1(text.encode()).hexdigest())
print("SHA256:", hashlib.sha256(text.encode()).hexdigest())
```

---

## 🔓 Password Cracking

### Step 1: Create Hash File

```bash
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hashes.txt
```

---

### Step 2: Run John the Ripper

```bash
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

---

### Step 3: Show Cracked Password

```bash
john --format=raw-md5 --show hashes.txt
```

---

### Expected Output

```text
5f4dcc3b5aa765d61d8327deb882cf99:password
```

---

## ⚔️ Attack Types

### 1. Dictionary Attack

```bash
john --wordlist=rockyou.txt hashes.txt
```

✔ Fast
✖ Limited to wordlist

---

### 2. Brute Force Attack

```bash
john --incremental hashes.txt
```

✔ No wordlist needed
✖ Very slow

---

### 3. Hybrid Attack

```bash
john --wordlist=rockyou.txt --rules hashes.txt
```

✔ More effective
✔ Uses mutations

---

## ❗ Common Errors & Fixes

### ❌ Incorrect Syntax

```bash
john --wordlist = path
```

### ✅ Correct Syntax

```bash
john --wordlist=path
```

---

### ❌ Hash Not Cracking

Reasons:

* Wrong hash
* Wrong format
* Password not in wordlist

---

### ✅ Fix: Specify Format

```bash
john --format=raw-md5 hashes.txt
```

---

### ✅ Verify Hash File

```bash
cat hashes.txt
```

---

## 🔐 Security Insights

* Hashing is NOT encryption
* Hashes cannot be reversed directly
* Weak passwords are easily crackable
* Strong hashing algorithms improve security

---

## 🚀 Future Scope

* Hashcat (GPU-based cracking)
* Salting techniques
* Rainbow tables
* Advanced password attacks

---

## 🧾 Conclusion

This lab provided hands-on experience with:

* Hash generation
* Password cracking techniques
* Understanding real-world vulnerabilities

---

## 👨‍💻 Author

**Subham Kar**
Cybersecurity Enthusiast 🚀

---

## ⭐ Support

If you found this useful:

* Star ⭐ the repository
* Share with others
* Keep learning & building

---
