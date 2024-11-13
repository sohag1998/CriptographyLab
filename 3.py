def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted_text += char
    
    return encrypted_text

def brute_force_caesar(ciphertext):
    print("Attempting all possible shifts for decryption:")
    for shift in range(26):
        decrypted_text = ""
        
        for char in ciphertext:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - offset - shift) % 26 + offset)
            else:
                decrypted_text += char
        
        print(f"Shift {shift}: {decrypted_text}")

# Example usage
plaintext = "Hello, World!"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)

print("Original Message:", plaintext)
print("Encrypted Message:", ciphertext)
print("\nBrute Force Decryption Attempts:")
brute_force_caesar(ciphertext)
