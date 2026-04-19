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