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
    plaintext = ""
    for i in range(len(ciphertext)):
        shift = ord(keyword[i % len(keyword)])
        if ciphertext[i] >= 'A' and ciphertext[i] <= 'Z':
            shift -= ord('A')
            if ord(ciphertext[i]) - shift >= ord('A'):
                plaintext += chr(ord(ciphertext[i]) - shift)
            else:
                plaintext += chr(ord('Z') - ord('A') + ord(ciphertext[i]) - shift + 1)
        elif ciphertext[i] >= 'a' and ciphertext[i] <= 'z':
            shift -= ord('a')
            if ord(ciphertext[i]) - shift >= ord('a'):
                plaintext += chr(ord(ciphertext[i]) - shift)
            else:
                plaintext += chr(ord('z') - ord('a') + ord(ciphertext[i]) - shift + 1)
        else:
            plaintext += ciphertext[i]
    return plaintext
