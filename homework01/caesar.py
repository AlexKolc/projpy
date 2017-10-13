def encrypt_caesar(plaintext, shift):
    """
    >>> encrypt_caesar("PYTHON", 26)
    'PYTHON'
    >>> encrypt_caesar("python", 0)
    'python'
    >>> encrypt_caesar("Python3.6", 3)
    'Sbwkrq3.6'
    >>> encrypt_caesar("", 3)
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if i >= 'A' and i <= 'Z':
            if ord(i) + shift <= ord('Z'):
                ciphertext += chr(ord(i) + shift)
            else:
                ciphertext += chr((ord(i) + shift) % ord('Z') + ord('A') - 1)
        elif i >= 'a' and i <= 'z':
            if ord(i) + shift <= ord('z'):
                ciphertext += chr(ord(i) + shift)
            else:
                ciphertext += chr((ord(i) + shift) % ord('z') + ord('a') - 1)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    >>> decrypt_caesar("SBWKRQ", 0)
    'SBWKRQ'
    >>> decrypt_caesar("sbwkrq", 0)
    'sbwkrq'
    >>> decrypt_caesar("Sbwkrq3.6", 3)
    'Python3.6'
    >>> decrypt_caesar("", 3)
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if i >= 'A' and i <= 'Z':
            if ord(i) - shift >= ord('A'):
                plaintext += chr(ord(i) - shift)
            else:
                plaintext += chr(ord('Z') - ord('A') + ord(i) - shift + 1)
        elif i >= 'a' and i <= 'z':
            if ord(i) - shift >= ord('a'):
                plaintext += chr(ord(i) - shift)
            else:
                plaintext += chr(ord('z') - ord('a') + ord(i) - shift + 1)
        else:
            plaintext += i
    return plaintext
