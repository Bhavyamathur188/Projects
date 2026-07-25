import random
import string


def generate_password(length, uppercase, lowercase, digits, symbols):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=" * 40)
print("       PASSWORD GENERATOR")
print("=" * 40)

while True:
    try:
        length = int(input("\nEnter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            continue

        uppercase = input("Include Uppercase Letters? (y/n): ").lower() == "y"
        lowercase = input("Include Lowercase Letters? (y/n): ").lower() == "y"
        digits = input("Include Numbers? (y/n): ").lower() == "y"
        symbols = input("Include Special Characters? (y/n): ").lower() == "y"

        password = generate_password(
            length,
            uppercase,
            lowercase,
            digits,
            symbols
        )

        if password is None:
            print("\nPlease select at least one character type.")
        else:
            print("\nGenerated Password:")
            print(password)

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")