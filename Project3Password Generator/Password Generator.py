import os
import random
import string

def generate_password(length: int) -> str:
    # Define the characters that can appear in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using os.urandom for cryptographic security
    # Alternatively, you can use random.choice if security isn't a major concern
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage
password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)
print(f"Generated password: {password}")
