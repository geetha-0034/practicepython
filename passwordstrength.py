import re
def check_password_strength(password):
    rules = [
        (len(password) >= 8, "Add at least 8 characters."),
        (re.search(r"[A-Z]", password), "Include at least one uppercase letter."),
        (re.search(r"[a-z]", password), "Include at least one lowercase letter."),
        (re.search(r"[0-9]", password), "Include at least one digit."),
        (re.search(r"[!@#$%^&*(),.?\":{}|<>]", password), "Include at least one special character."),
    ]
    errors = [msg for passed, msg in rules if not passed]
    
    if errors:
        print(f"Weak Password: {password}")
        for err in errors:
            print(f"- {err}")
    else:
        print(f"Strong Password: {password}")
    
pwd = input("Enter your password: ")
check_password_strength(pwd)     