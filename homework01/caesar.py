def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i] >= 'A' and plaintext[i] <= 'Z':
            if ord(plaintext[i]) + 3 <= ord('Z'):
                ciphertext += chr(ord(plaintext[i]) + 3)
            else:
                ciphertext += chr((ord(plaintext[i]) + 3) % ord('Z') + ord('A') - 1)
        elif plaintext[i] >= 'a' and plaintext[i] <= 'z':
            if ord(plaintext[i]) + 3 <= ord('z'):
                ciphertext += chr(ord(plaintext[i]) + 3)
            else:
                ciphertext += chr((ord(plaintext[i]) + 3) % ord('z') + ord('a') - 1)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i] >= 'A' and ciphertext[i] <= 'Z':
            if ord(ciphertext[i]) - 3 >= ord('A'):
                plaintext += chr(ord(ciphertext[i]) - 3)
            else:
                plaintext += chr(ord('Z') - ord('A') + ord(ciphertext[i]) - 3 + 1)
        elif ciphertext[i] >= 'a' and ciphertext[i] <= 'z':
            if ord(ciphertext[i]) - 3 >= ord('a'):
                plaintext += chr(ord(ciphertext[i]) - 3)
            else:
                plaintext += chr(ord('z') - ord('a') + ord(ciphertext[i]) - 3 + 1)
        else:
            plaintext += ciphertext[i]
    return plaintext
