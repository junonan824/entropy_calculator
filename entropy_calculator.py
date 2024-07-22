
#### `entropy_calculator.py`
import math
from collections import Counter

def calculate_entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def get_letter_probabilities(text):
    letter_counts = Counter(text)
    total_letters = sum(letter_counts.values())
    probabilities = {char: count / total_letters for char, count in letter_counts.items()}
    return probabilities

def text_entropy(text):
    cleaned_text = text.replace(" ", "").replace("\n", "").lower()
    letter_probabilities = get_letter_probabilities(cleaned_text)
    probabilities = list(letter_probabilities.values())
    return calculate_entropy(probabilities)

def password_entropy(password):
    pool_size = 0
    if any(char.islower() for char in password):
        pool_size += 26
    if any(char.isupper() for char in password):
        pool_size += 26
    if any(char.isdigit() for char in password):
        pool_size += 10
    if any(char in '!@#$%^&*()-_+=<>?' for char in password):
        pool_size += len('!@#$%^&*()-_+=<>?')
    return len(password) * math.log2(pool_size)

if __name__ == "__main__":
    choice = input("Calculate entropy for (1) Text or (2) Password? ")
    if choice == "1":
        text = input("Enter the text: ")
        entropy = text_entropy(text)
        print(f"The entropy of the given text is: {entropy:.2f} bits")
    elif choice == "2":
        password = input("Enter the password: ")
        entropy = password_entropy(password)
        print(f"The entropy of the given password is: {entropy:.2f} bits")
    else:
        print("Invalid choice. Please select 1 or 2.")
