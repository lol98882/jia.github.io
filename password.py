
import random
import string

def generate_password(length=12):
    if length < 6:
        print("Password too short! Must be at least 6 characters.")
        return None

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)

    return ''.join(password)

print( generate_password(12))
                     #
      

