def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
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
    for char in plaintext:
        if "A" <= char <= "Z":
            shifted = ord(char) - ord("A")
            shifted = (shifted + shift) % 26
            ciphertext += chr(ord("A") + shifted)
        elif "a" <= char <= "z":
            shifted = ord(char) - ord("a")
            shifted = (shifted + shift) % 26
            ciphertext += chr(ord("a") + shifted)
        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
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
    plaintext = ""

    for char in ciphertext:
        if "A" <= char <= "Z":
            shifted = ord(char) - ord("A")
            shifted = (shifted - shift) % 26
            plaintext += chr(ord("A") + shifted)
        elif "a" <= char <= "z":
            shifted = ord(char) - ord("a")
            shifted = (shifted - shift) % 26
            plaintext += chr(ord("a") + shifted)
        else:
            plaintext += char
    return plaintext
