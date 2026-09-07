"""
app.py
------
The web version of the Password Strength Checker, built with Flask.

Flask is a small, beginner-friendly Python web framework. This file:
  1. Starts a local web server.
  2. Shows the HTML page (templates/index.html) when you visit the site.
  3. Exposes a small API endpoint (/check) that the page's JavaScript calls
     every time you type, so the strength meter updates live.

Run it with:
    python app.py

Then open the link it prints (usually http://127.0.0.1:5000) in your browser.
"""

from flask import Flask, render_template, request, jsonify
from password_checker import check_password_strength

app = Flask(__name__)


@app.route("/")
def home():
    """Show the main page."""
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    """
    Receive a password from the browser (as JSON), run it through
    check_password_strength(), and send the result back as JSON.
    """
    data = request.get_json(silent=True) or {}
    password = data.get("password", "")
    result = check_password_strength(password)
    return jsonify(result)


if __name__ == "__main__":
    # debug=True auto-reloads the server whenever you save a file,
    # which is very handy while learning/experimenting.
    app.run(debug=True)
