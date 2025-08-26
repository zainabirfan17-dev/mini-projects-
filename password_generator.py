import re        # regex module → lets us define patterns like \d, [A-Z], etc.
import secrets   # cryptographically secure random generator
import string    # has constants like ascii_letters, digits, punctuation

def generate_password(length=16,nums=1,uppercase=1,lowercase=1,special_char=1):
    """
    Generate a secure random password with the following rules:
    - Must include at least one digit
    - Must include at least one special character
    - Must include at least one uppercase letter
    - Must include at least one lowercase letter
    """

    # Define character sets
    letters = string.ascii_letters      # all uppercase + lowercase letters
    digits = string.digits              # "0123456789"
    symbols = string.punctuation        # "!@#$%...etc"

    # Combine everything for random choice
    all_characters = letters + digits + symbols

    # Define requirements as (minimum_required, regex_pattern)
    constants = [
        (nums, r"\d"),          # at least 1 digit
        (special_char, rf"[{symbols}]"), # at least 1 special char
        (uppercase, r"[A-Z]"),       # at least 1 uppercase
        (lowercase, r"[a-z]")        # at least 1 lowercase
    ]

    # Keep generating until a valid password is created
    while True:
        password = ""

        # Build password of required length
        for _ in range(length):
           password +=secrets.choice(all_characters)


        # Validate password against all requirements
        if all(
            count <= len(re.findall(pattern, password))
            for count, pattern in constants
        ):
            return password  # ✅ valid password found


# Example usage
secure_pass = generate_password()
print("Generated password:", secure_pass)
