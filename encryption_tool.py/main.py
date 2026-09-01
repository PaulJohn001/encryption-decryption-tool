def encrypt_text(text, shift=3):
    """Encrypt a message using a Caesar cipher."""
    encrypted_chars = []

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            position = ord(char) - start
            shifted = (position + shift) % 26
            encrypted_chars.append(chr(start + shifted))
        else:
            encrypted_chars.append(char)

    return ''.join(encrypted_chars)


def decrypt_text(text, shift=3):
    """Decrypt a Caesar cipher message."""
    decrypted_chars = []

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            position = ord(char) - start
            shifted = (position - shift) % 26
            decrypted_chars.append(chr(start + shifted))
        else:
            decrypted_chars.append(char)

    return ''.join(decrypted_chars)


if __name__ == "__main__":
    user_text = input("Enter text to encrypt: ")
    shift = 3

    encrypted_text = encrypt_text(user_text, shift)
    decrypted_text = decrypt_text(encrypted_text, shift)

    print("\nOriginal text:", user_text)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
