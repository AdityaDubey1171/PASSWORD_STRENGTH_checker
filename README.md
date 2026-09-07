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

---

## 🖥️ Part 1 — Setting up VS Code

1. **Install VS Code** (if you haven't): [code.visualstudio.com](https://code.visualstudio.com)
2. **Install Python** (if you haven't): [python.org/downloads](https://www.python.org/downloads/) — during install, tick **"Add Python to PATH"**.
3. Open VS Code, then install the **Python extension**:
   - Click the Extensions icon on the left sidebar (looks like 4 squares)
   - Search "Python" (by Microsoft) → Install
4. **Open this project folder** in VS Code:
   - `File → Open Folder...` → select the `password-strength-checker` folder

---

## ▶️ Part 2 — Running the project

Open a terminal inside VS Code: `Terminal → New Terminal` (or `` Ctrl+` ``).

### Option A: Terminal version (easiest, no install needed)

```bash
python cli.py
```

Type a password when prompted, press Enter, and see the result. Type
`exit` to quit.

### Option B: Website version

**Step 1 — Create a virtual environment** (a clean, isolated space for this
project's packages, so it doesn't affect other Python projects on your
computer):

```bash
python -m venv venv
```

**Step 2 — Activate it:**

- Windows (PowerShell):
  ```bash
  venv\Scripts\activate
  ```
- macOS / Linux:
  ```bash
  source venv/bin/activate
  ```
You'll know it worked because you'll see `(venv)` at the start of your
terminal line.

**Step 3 — Install Flask:**

```bash
pip install -r requirements.txt
```

**Step 4 — Run the app:**

```bash
python app.py
```

**Step 5 — Open your browser** and go to the link shown in the terminal
(usually `http://127.0.0.1:5000`). Start typing a password and watch the
meter update live!

To stop the server, click back in the terminal and press `Ctrl+C`.

---

## 📤 Part 3 — Pushing this project to GitHub

**Step 1 — Create a GitHub account** (skip if you have one): [github.com](https://github.com)

**Step 2 — Create a new empty repository on GitHub:**
1. Click the `+` icon (top right) → **New repository**
2. Name it e.g. `password-strength-checker`
3. Leave it **empty** (don't add a README/gitignore there — we already have our own)
4. Click **Create repository**
5. Copy the repository URL it shows you, e.g.
   `https://github.com/your-username/password-strength-checker.git`

**Step 3 — Install Git** (if you don't have it): [git-scm.com/downloads](https://git-scm.com/downloads)

**Step 4 — In the VS Code terminal, inside your project folder, run:**

```bash
git init
git add .
git commit -m "Initial commit: password strength checker mini project"
git branch -M main
git remote add origin https://github.com/your-username/password-strength-checker.git
git push -u origin main
```

Replace the URL in the `git remote add origin` line with **your own**
repository URL from Step 2. The first time you push, GitHub may open a
browser window asking you to log in — just follow the prompts.

**That's it!** Refresh your GitHub repository page and you'll see all your
files there.

### Making future changes
Whenever you edit the code later, save your changes to GitHub with:
```bash
git add .
git commit -m "Describe what you changed"
git push
```

---

## 🎤 Tips for presenting this at college

- Demo the **terminal version first** (`cli.py`) — it's easy to explain line
  by line.
- Then demo the **website version** — show the live meter changing as you type
  a weak password, then a strong one.
- Mention the design choices: separation of logic (`password_checker.py`)
  from interface (`cli.py` / `app.py` + `index.html`), the common-password
  blocklist, and the checklist that gives clear feedback.
- Good stretch goals to mention as "future improvements": checking against a
  much larger leaked-password database (like the Have I Been Pwned API),
  estimating "time to crack," or adding user accounts.

---

## 🛠️ Built with

- **Python 3** — core logic
- **Flask** — lightweight web framework
- **HTML/CSS/JavaScript** — front-end interface
