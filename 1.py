def encrypt(text, shift):
    encrypted_text = ""
    # Traverse the text
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            # Determine offset for uppercase or lowercase letters
            offset = 65 if char.isupper() else 97
            # Encrypt character and add to result
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Keep any non-alphabet characters as they are
            encrypted_text += char
            
    return encrypted_text
def decrypt(text, shift):
    decrypted_text = ""
    
    # Traverse the text
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            # Determine offset for uppercase or lowercase letters
            offset = 65 if char.isupper() else 97
            # Decrypt character and add to result
            decrypted_text += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            # Keep any non-alphabet characters as they are
            decrypted_text += char
            
    return decrypted_text
# Example Usage
plaintext = "Hello, World!"
shift = 3
encrypted_message = encrypt(plaintext, shift)
decrypted_message = decrypt(encrypted_message, shift)
print("Original Message:", plaintext)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)








Original Message: Hello, World!
Encrypted Message: Khoor, Zruog!
Decrypted Message: Hello, World!