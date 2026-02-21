import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&*]", password):
        strength += 1

    if strength == 5:
        return "Very Strong 🔥"
    elif strength >= 3:
        return "Strong 💪"
    elif strength == 2:
        return "Medium ⚠️"
    else:
        return "Weak ❌"


print("🔐 Password Strength Checker")

password = input("Enter your password: ")

result = check_password_strength(password)

print("Password Strength:", result) w
