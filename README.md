# PASSWORD_STRENGTH_checker
🔐 Password Strength Checker  A small project I built while learning more about cybersecurity and understanding what makes a password strong and secure.  Still learning, still building, and enjoying the process! 🛡️
# 🔐 Password Strength Checker (Python + Flask Mini Project)

A beginner-friendly college mini project that checks how strong a password
is, in two ways:

1. **`cli.py`** — a simple terminal program (start here!)
2. **`app.py`** — a full website version with a live strength meter, built
   with **Flask**, **HTML**, and **CSS**

---

## 📁 Project structure

```
password-strength-checker/
├── app.py                 # Flask web server (the website version)
├── cli.py                 # Terminal version (simplest, start here)
├── password_checker.py    # The actual strength-checking logic (used by both)
├── requirements.txt       # Python packages this project needs
├── .gitignore              # Tells Git which files to ignore
├── templates/
│   └── index.html         # The webpage's structure
└── static/
    └── style.css           # The webpage's styling
```

**Why is the logic in its own file (`password_checker.py`)?**
This is a common good practice called *separation of concerns* — the
"brain" of the project (checking the password) is kept separate from the
"interface" (terminal or website). It also means you can explain in your
presentation: *"I designed this so the same checking logic can power both a
terminal tool and a website."* That's a great point for a viva/demo.

---

## 🧠 How the strength check works

`password_checker.py` scores a password out of 6 points by checking:

| Rule | Points |
|---|---|
| At least 8 characters | 1 |
| At least 12 characters (bonus) | 1 |
| Contains a lowercase letter | 1 |
| Contains an uppercase letter | 1 |
| Contains a number | 1 |
| Contains a special character (!@#$...) | 1 |

Two extra penalties:
- If the password is in a list of very common leaked passwords (like
  `123456` or `password`), the score is forced to **0**.
- If it has a character repeated 3+ times in a row (like `aaaa`), 1 point
  is subtracted.

The score maps to a label: **Very Weak → Weak → Medium → Strong → Very
Strong**, and the function also returns specific tips (e.g. *"Add a special
character"*).



