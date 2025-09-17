import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add a special character.")

    if strength <= 2:
        return "Weak", feedback
    elif strength == 3 or strength == 4:
        return "Medium", feedback
    else:
        return "Strong", ["Good password!"]

# Example
if __name__ == "__main__":
    pwd = input("Enter a password: ")
    strength, tips = check_password_strength(pwd)
    print(f"Strength: {strength}")
    for t in tips:
        print(" -", t)
