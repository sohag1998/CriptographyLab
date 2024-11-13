import random
import string

def generate_random_key():
    alphabet = list(string.ascii_uppercase)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    
    return dict(zip(alphabet, shuffled_alphabet))


def encrypt(text, key):
    encrypted_text = ""
    
    # Traverse the text
    for char in text:
        if char.isalpha():  # Encrypt only alphabet characters
            # Convert to uppercase for standardization
            uppercase_char = char.upper()
            encrypted_char = key[uppercase_char]
            # Preserve original case
            encrypted_text += encrypted_char if char.isupper() else encrypted_char.lower()
        else:
            # Keep non-alphabet characters as they are
            encrypted_text += char
    
    return encrypted_text


def decrypt(text, key):
    # Reverse the key to decrypt
    reverse_key = {v: k for k, v in key.items()}
    decrypted_text = ""
    
    # Traverse the text
    for char in text:
        if char.isalpha():  # Decrypt only alphabet characters
            # Convert to uppercase for standardization
            uppercase_char = char.upper()
            decrypted_char = reverse_key[uppercase_char]
            # Preserve original case
            decrypted_text += decrypted_char if char.isupper() else decrypted_char.lower()
        else:
            # Keep non-alphabet characters as they are
            decrypted_text += char
            
    return decrypted_text

# Example Usage
plaintext = "Hello, World!"
key = generate_random_key()  # Generate a random substitution key

encrypted_message = encrypt(plaintext, key)
decrypted_message = decrypt(encrypted_message, key)

print("Original Message:", plaintext)
print("Encryption Key:", key)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
