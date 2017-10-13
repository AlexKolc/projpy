def encrypt_caesar(plaintext, shift):
    """
    >>> encrypt_caesar("PYTHON", 3)
    'SBWKRQ'
    >>> encrypt_caesar("python", 3)
    'sbwkrq'
    >>> encrypt_caesar("Python3.6", 3)
    'Sbwkrq3.6'
    >>> encrypt_caesar("", 3)
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if i >= 'A' and i <= 'Z':
            if ord(i) + 3 <= ord('Z'):
                ciphertext += chr(ord(i) + shift)
            else:
                ciphertext += chr((ord(i) + shift) % ord('Z') + ord('A') - 1)
        elif i >= 'a' and i <= 'z':
            if ord(i) + 3 <= ord('z'):
                ciphertext += chr(ord(i) + shift)
            else:
                ciphertext += chr((ord(i) + shift) % ord('z') + ord('a') - 1)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    >>> decrypt_caesar("SBWKRQ", 3)
    'PYTHON'
    >>> decrypt_caesar("sbwkrq", 3)
    'python'
    >>> decrypt_caesar("Sbwkrq3.6", 3)
    'Python3.6'
    >>> decrypt_caesar("", 3)
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if i >= 'A' and i <= 'Z':
            if ord(i) - 3 >= ord('A'):
                plaintext += chr(ord(i) - shift)
            else:
                plaintext += chr(ord('Z') - ord('A') + ord(i) - shift + 1)
        elif i >= 'a' and i <= 'z':
            if ord(i) - 3 >= ord('a'):
                plaintext += chr(ord(i) - shift)
            else:
                plaintext += chr(ord('z') - ord('a') + ord(i) - shift + 1)
        else:
            plaintext += i
    return plaintext
