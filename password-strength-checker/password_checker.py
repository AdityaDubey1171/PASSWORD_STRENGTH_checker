"""
password_checker.py
--------------------
Core logic for the Password Strength Checker mini project.

This file has ZERO dependency on Flask or any web framework, so it can be
imported by:
  1. cli.py          -> run it in a terminal
  2. app.py           -> run it as a web app

Keeping the "brain" of the project separate from the "interface" (terminal
or website) is a common and good practice called SEPARATION OF CONCERNS.
"""

import re

# A very small sample list of extremely common / leaked passwords.
# In a real product this list would have thousands of entries and would be
# loaded from a file, but a short list is enough to demonstrate the idea.
COMMON_PASSWORDS = {
    "123456", "123456789", "password", "12345678", "qwerty",
    "111111", "12345", "abc123", "1234567", "password1",
    "iloveyou", "admin", "welcome", "monkey", "login",
}


def check_password_strength(password: str) -> dict:
    """
    Analyse a password and return a dictionary describing how strong it is.

    Returns
    -------
    dict with keys:
        score      : int   -> 0 to 6  (higher = stronger)
        max_score  : int   -> 6
        label      : str   -> "Very Weak" / "Weak" / "Medium" / "Strong" / "Very Strong"
        percent    : int   -> score expressed as a percentage, handy for a progress bar
        feedback   : list[str] -> tips on how to improve the password
        checks     : dict  -> True/False result for every individual rule
    """
    feedback = []
    score = 0

    length = len(password)

    # ---- Rule 1: length -----------------------------------------------
    has_min_length = length >= 8
    has_good_length = length >= 12
    if has_min_length:
        score += 1
    else:
        feedback.append("Use at least 8 characters (12+ is even better).")

    if has_good_length:
        score += 1

    # ---- Rule 2: character variety -------------------------------------
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?`~]", password))

    if has_lower:
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if has_upper:
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if has_digit:
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if has_symbol:
        score += 1
    else:
        feedback.append("Add at least one special character (e.g. ! @ # $ %).")

    # ---- Rule 3: not a common / leaked password ------------------------
    is_common = password.lower() in COMMON_PASSWORDS
    if is_common:
        score = 0  # an extremely common password is always "Very Weak"
        feedback.insert(0, "This password is extremely common and easy to guess. Avoid it.")

    # ---- Rule 4: no obvious repeated characters (aaaa, 1111, ...) ------
    has_repeats = bool(re.search(r"(.)\1{2,}", password))
    if has_repeats:
        score = max(score - 1, 0)
        feedback.append("Avoid repeating the same character 3+ times in a row.")

    max_score = 6
    score = max(0, min(score, max_score))
    percent = int((score / max_score) * 100)

    if password == "":
        label = "No password entered"
    elif score <= 1:
        label = "Very Weak"
    elif score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    elif score <= 5:
        label = "Strong"
    else:
        label = "Very Strong"

    if not feedback and password:
        feedback.append("Great job! This is a strong password.")

    return {
        "score": score,
        "max_score": max_score,
        "label": label,
        "percent": percent,
        "feedback": feedback,
        "checks": {
            "min_length_8": has_min_length,
            "good_length_12": has_good_length,
            "has_lowercase": has_lower,
            "has_uppercase": has_upper,
            "has_digit": has_digit,
            "has_symbol": has_symbol,
            "is_common_password": is_common,
            "has_repeated_chars": has_repeats,
        },
    }


if __name__ == "__main__":
    # Quick manual test if you just run: python password_checker.py
    sample = "Password123!"
    result = check_password_strength(sample)
    print(f"Password: {sample}")
    print(f"Strength: {result['label']} ({result['score']}/{result['max_score']})")
    for tip in result["feedback"]:
        print(f" - {tip}")
