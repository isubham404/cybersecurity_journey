# Day 10 - Web-Based Password Strength Checker

---

## Objective

To build a real-time password strength checker as a web application using HTML, CSS, and JavaScript. The goal is to convert previously implemented Python logic into a browser-based interactive tool.

---

## Introduction

Earlier implementations of the password checker were done using Python in a terminal environment. This project extends that logic to a web interface, allowing users to receive instant feedback while typing their password.

This marks the transition from command-line applications to web-based applications.

---

## Technologies Used

1. HTML (Structure of the webpage)
2. CSS (Styling and layout)
3. JavaScript (Logic and interactivity)

---

## Project Structure

```
password-checker-web/
│
├── index.html
├── style.css
└── script.js
```

---

## HTML Structure

### Purpose

Defines the layout of the webpage including input field and output sections.

### Key Elements

* Input field for password
* Paragraph to display strength
* List to display feedback

### Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>Password Checker</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <h2>Password Strength Checker</h2>

    <input type="password" id="password" placeholder="Enter password">

    <p id="strength"></p>
    <ul id="feedback"></ul>
</div>

<script src="script.js"></script>
</body>
</html>
```

---

## CSS Styling

### Purpose

Improves the appearance of the webpage.

### Features

* Centered layout
* Dark theme
* Styled input field

### Code

```css
body {
    font-family: Arial;
    background: #111;
    color: white;
    text-align: center;
    margin-top: 100px;
}

input {
    padding: 10px;
    width: 250px;
    margin: 10px;
}

.container {
    max-width: 400px;
    margin: auto;
}
```

---

## JavaScript Logic

### Purpose

Implements real-time password analysis and feedback.

---

## Key Concepts

### 1. Event Listener

```javascript
passwordInput.addEventListener("input", function ()
```

This triggers the function every time the user types in the input field.

---

### 2. Password Validation Rules

The password is checked for:

* Minimum length (8 characters)
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Each condition increases the score.

---

### 3. Regular Expressions

Used for pattern matching:

* /[A-Z]/ → checks uppercase
* /[a-z]/ → checks lowercase
* /[0-9]/ → checks digits
* /[^A-Za-z0-9]/ → checks symbols

---

### 4. Score Calculation

Each satisfied condition adds 1 point.

---

### 5. Strength Classification

| Score | Strength |
| ----- | -------- |
| 0–2   | Weak     |
| 3–4   | Medium   |
| 5     | Strong   |

---

### 6. Feedback System

Suggestions are stored in an array and displayed dynamically.

---

## JavaScript Code

```javascript
const passwordInput = document.getElementById("password");
const strengthText = document.getElementById("strength");
const feedbackList = document.getElementById("feedback");

passwordInput.addEventListener("input", function () {
    const password = passwordInput.value;
    let score = 0;
    let feedback = [];

    if (password.length >= 8) score++;
    else feedback.push("At least 8 characters");

    if (/[A-Z]/.test(password)) score++;
    else feedback.push("Add uppercase letter");

    if (/[a-z]/.test(password)) score++;
    else feedback.push("Add lowercase letter");

    if (/[0-9]/.test(password)) score++;
    else feedback.push("Add number");

    if (/[^A-Za-z0-9]/.test(password)) score++;
    else feedback.push("Add special character");

    let strength = "";

    if (score === 5) strength = "Strong";
    else if (score >= 3) strength = "Medium";
    else strength = "Weak";

    strengthText.textContent = "Strength: " + strength;

    feedbackList.innerHTML = "";
    feedback.forEach(item => {
        let li = document.createElement("li");
        li.textContent = item;
        feedbackList.appendChild(li);
    });
});
```

---

## Key Differences from Python Version

| Feature       | Python Version | Web Version        |
| ------------- | -------------- | ------------------ |
| Execution     | Terminal       | Browser            |
| Interaction   | Manual input   | Real-time typing   |
| Output        | Printed text   | Dynamic UI updates |
| Language Used | Python         | JavaScript         |

---

## Learning Outcome

* Learned how to convert logic from Python to JavaScript
* Understood DOM manipulation
* Implemented real-time event handling
* Built an interactive web application
* Learned basic frontend structure

---

## Limitations

* No backend integration
* No data storage
* No password history checking
* Basic UI design

---

## Future Improvements

* Add color-based strength indicator
* Add strength progress bar
* Integrate backend using Python (Flask)
* Store user data securely
* Build complete login system

---

## Conclusion

This project marks the transition from basic programming to web development. It demonstrates how cybersecurity-related logic can be applied in a real-time web environment, forming the foundation for full-stack development.
