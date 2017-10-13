def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        shift = ord(keyword[i % len(keyword)])
        if plaintext[i] >= 'A' and plaintext[i] <= 'Z':
            shift -= ord('A')
            if ord(plaintext[i]) + shift <= ord('Z'):
                ciphertext += chr(ord(plaintext[i]) + shift)
            else:
                ciphertext += chr((ord(plaintext[i]) + shift) % ord('Z') + ord('A') - 1)
        elif plaintext[i] >= 'a' and plaintext[i] <= 'z':
            shift -= ord('a')
            if ord(plaintext[i]) + shift <= ord('z'):
                ciphertext += chr(ord(plaintext[i]) + shift)
            else:
                ciphertext += chr((ord(plaintext[i]) + shift) % ord('z') + ord('a') - 1)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    return plaintext
