import re

def check_strength(password):
    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([has_upper, has_lower, has_digit, has_special])

    # Strength logic
    if length < 6:
        return "Weak"
    elif score >= 3 and length >= 8:
        return "Strong"
    elif score >= 2:
        return "Moderate"
    else:
        return "Weak"

def give_feedback(password):
    feedback = []
    if not re.search(r"[A-Z]", password):
        feedback.append("Add at least one UPPERCASE letter.")
    if not re.search(r"[a-z]", password):
        feedback.append("Add at least one lowercase letter.")
    if not re.search(r"\d", password):
        feedback.append("Include at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Use special characters like @, #, $ etc.")
    if len(password) < 8:
        feedback.append("Make the password at least 8 characters long.")

    return feedback if feedback else ["Great! Your password is strong."]

def main():
    print("🔐 Password Complexity Checker")
    password = input("Enter a password to check: ")
    strength = check_strength(password)
    print(f"\n🛡️ Strength: {strength}\n")

    print("🧠 Suggestions:")
    for tip in give_feedback(password):
        print(f" - {tip}")

if __name__ == "__main__":
    main()
