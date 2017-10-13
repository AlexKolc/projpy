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
    for i in plaintext:
        if i >= 'A' and i <= 'Z':
            if ord(i) + 3 <= ord('Z'):
                ciphertext += chr(ord(i) + 3)
            else:
                ciphertext += chr((ord(i) + 3) % ord('Z') + ord('A') - 1)
        elif i >= 'a' and i <= 'z':
            if ord(i) + 3 <= ord('z'):
                ciphertext += chr(ord(i) + 3)
            else:
                ciphertext += chr((ord(i) + 3) % ord('z') + ord('a') - 1)
        else:
            ciphertext += i
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
    for i in ciphertext:
        if i >= 'A' and i <= 'Z':
            if ord(i) - 3 >= ord('A'):
                plaintext += chr(ord(i) - 3)
            else:
                plaintext += chr(ord('Z') - ord('A') + ord(i) - 3 + 1)
        elif i >= 'a' and i <= 'z':
            if ord(i) - 3 >= ord('a'):
                plaintext += chr(ord(i) - 3)
            else:
                plaintext += chr(ord('z') - ord('a') + ord(i) - 3 + 1)
        else:
            plaintext += i
    return plaintext
