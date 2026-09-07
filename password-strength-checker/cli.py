"""
cli.py
------
The simplest way to use this project: a terminal program.

Run it with:
    python cli.py

This is a great first step before touching the web version, because you can
see the core logic (password_checker.py) working with no HTML/CSS involved.
"""

from password_checker import check_password_strength


def main():
    print("=" * 50)
    print(" PASSWORD STRENGTH CHECKER (Terminal Version) ")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    while True:
        password = input("Enter a password to check: ")
        if password.lower() == "exit":
            print("Goodbye!")
            break

        result = check_password_strength(password)

        print(f"\nStrength: {result['label']}  "
              f"({result['score']}/{result['max_score']} points, "
              f"{result['percent']}%)")
        print("Feedback:")
        for tip in result["feedback"]:
            print(f"  - {tip}")
        print("-" * 50)


if __name__ == "__main__":
    main()
