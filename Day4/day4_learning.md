# 🔐 Day 4 - Caesar Cipher (Encryption Basics)

## 📌 What is Encryption?

Encryption is the process of converting readable data (plain text) into an unreadable format (cipher text) to protect information.

### 👉 Example:

* Original Text: HELLO
* Encrypted Text: KHOOR

Only someone who knows the method (key) can convert it back.

---

## 📌 Why is Encryption Important?

* Protects passwords 🔑
* Secures online communication 🌐
* Used in banking, messaging apps, websites

👉 Without encryption, anyone could read your data.

---

## 📌 What is Caesar Cipher?

Caesar Cipher is one of the simplest encryption techniques.

👉 It works by **shifting each letter** in the text by a fixed number.

---

### 🧠 Example (Shift = 3)

| Original | Encrypted |
| -------- | --------- |
| A        | D         |
| B        | E         |
| C        | F         |

So:

* HELLO → KHOOR

---

## 📌 Logic Behind the Code

### Step 1: Take input from user

We ask the user to enter some text.

---

### Step 2: Loop through each character

We use a loop:

```python
for char in text:
```

👉 This processes one letter at a time.

---

### Step 3: Check if character is a letter

```python
if char.isalpha():
```

👉 This ensures:

* Only letters are shifted
* Numbers/symbols remain unchanged

---

### Step 4: Convert letter to number

```python
ord(char)
```

👉 Example:

* A → 65
* B → 66

---

### Step 5: Shift the value

```python
ord(char) + shift
```

👉 Moves the letter forward

---

### Step 6: Convert back to character

```python
chr(new_value)
```

👉 Example:

* 68 → D

---

### Step 7: Store result

We add each new letter to a string:

```python
result += new_char
```

---

## 📌 Key Functions Used

| Function  | Purpose                |
| --------- | ---------------------- |
| input()   | Take user input        |
| for loop  | Process each character |
| isalpha() | Check if letter        |
| ord()     | Convert char → number  |
| chr()     | Convert number → char  |

---

## 📌 What I Learned Today

* Basic concept of encryption
* How Caesar Cipher works
* How to loop through a string
* How characters are converted using ASCII
* How simple encryption logic is implemented in Python

---

## 📌 Limitations of Caesar Cipher

* Very easy to break ❌
* Not secure for real-world use ❌

👉 Used only for learning purposes.

---

## 🚀 Conclusion

Today I learned how encryption works at a basic level and implemented my first encryption algorithm using Python.

This is my first step towards understanding cybersecurity concepts.
