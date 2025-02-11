import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    if length < 4:
        return "Password length should be at least 4 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to take user input and generate password."""
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
