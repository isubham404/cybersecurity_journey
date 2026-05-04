# 🔐 XSS Lab – Cookie Theft Simulation (HTML + JavaScript)

## 📌 Objective

To understand and demonstrate how **Cross-Site Scripting (XSS)** works by:

* Creating a vulnerable web page
* Injecting malicious input
* Accessing browser cookies
* Understanding impact and prevention

---

## 🧠 What is XSS?

**Cross-Site Scripting (XSS)** is a vulnerability where:

> A web application allows users to inject and execute malicious JavaScript in a browser.

---

## 🧪 Lab Setup

### 📁 File Created

`index.html`

### 🧾 Vulnerable Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>XSS Lab</title>
</head>
<body>

<h2>Search Page</h2>

<input type="text" id="input">
<button onclick="display()">Search</button>

<p id="result"></p>

<script>
// Simulated cookie
document.cookie = "user=admin123";

function display() {
    let userInput = document.getElementById("input").value;

    // ❌ Vulnerable line
    document.getElementById("result").innerHTML = userInput;
}
</script>

</body>
</html>
```

---

## ⚠️ Vulnerability Explanation

```js
innerHTML = userInput
```

* Directly inserts user input into the DOM
* Browser interprets input as HTML/JavaScript
* No validation or sanitization

👉 This allows execution of malicious scripts

---

## 🧪 Exploitation

### ✅ Working Payload

```html
<img src=x onerror=alert(document.cookie)>
```

---

## 📸 Output Observed

* Popup displayed in browser
* Cookies extracted successfully

Example:

```
user=admin123;
_ga=...;
_ga_69MPZE94D5=...
```

---

## 🧠 Why `<script>` Did Not Work?

```html
<script>alert(1)</script>
```

* Modern browsers may block inline `<script>` execution in some contexts
* Event-based payloads bypass these restrictions

---

## 🔥 XSS Bypass Technique Used

```html
<img src=x onerror=alert(1)>
```

* Uses HTML event handler (`onerror`)
* Executes JavaScript when image fails to load
* More reliable than `<script>` tag in many cases

---

## 🎯 Impact of This Vulnerability

If this occurs on a real website:

* 🔓 Session hijacking
* 👤 Account takeover
* 📄 Access to sensitive data
* 🎭 Impersonation of users

---

## 🛡️ Prevention (Fix)

### ✅ Secure Code

```js
document.getElementById("result").innerText = userInput;
```

---

### 🔐 Why This Works

| Method    | Behavior                 |
| --------- | ------------------------ |
| innerHTML | Executes HTML/JS ❌       |
| innerText | Displays as plain text ✅ |

---

## 🧠 Key Learnings

* XSS occurs due to **unsanitized user input**
* Not all payloads behave the same (`<script>` vs event-based)
* Cookies can be accessed via `document.cookie`
* Real attackers use **bypass techniques**
* Defense is as important as exploitation

---

## 🚀 Real-World Insight

Attackers rarely use:

```html
<script>alert(1)</script>
```

They prefer:

```html
<img src=x onerror=...>
```

👉 Because it works in more scenarios

---

## 📌 Lab Summary

| Step | Action                     |
| ---- | -------------------------- |
| 1    | Created vulnerable page    |
| 2    | Injected malicious payload |
| 3    | Executed JavaScript        |
| 4    | Accessed cookies           |
| 5    | Fixed vulnerability        |

---

## 🧠 Next Steps

* Stored XSS (persistent attack)
* XSS + phishing simulation
* Session hijacking concepts
* Content Security Policy (CSP)

---

## ⚠️ Disclaimer

This lab is performed in a **controlled environment** for educational purposes only.
Do NOT test on real websites without permission.

---

## 👨‍💻 Author

Subham Kar
Cybersecurity Journey – Day 18

---
