def is_valid_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    return has_upper and has_lower and has_digit

password = input("Enter your password: ")
if is_valid_password(password):
    print("Valid password!")
else:
    print("Invalid password. Passwords must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")
