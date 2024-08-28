# Star Dollar Algorithm

# Mapping of characters to symbol sequences
star_dollar_map = {
    'A': '$1',
    'B': '*1',
    'C': '$$1',
    'D': '**1',
    'E': '$$$1',
    'F': '****1',
    'G': '$$$$1',
    'H': '*****1',
    'I': '$$$$$1',
    'J': '******1',
    'K': '$$$$$$1',
    'L': '********1',
    'M': '$$$$$$$$1',
    'N': '*********1',
    'O': '$$$$$$$$$1',
    'P': '**********1',
    'Q': '$$$$$$$$$$1',
    'R': '***********1',
    'S': '$$$$$$$$$$$1',
    'T': '*************1',
    'U': '$$$$$$$$$$$$$1',
    'V': '**************1',
    'W': '$$$$$$$$$$$$$$1',
    'X': '***************1',
    'Y': '$$$$$$$$$$$$$$$$1',
    'Z': '****************1',
    'a': '$2',
    'b': '*2',
    'c': '$$2',
    'd': '**2',
    'e': '$$$2',
    'f': '****2',
    'g': '$$$$2',
    'h': '*****2',
    'i': '$$$$$2',
    'j': '******2',
    'k': '$$$$$$2',
    'l': '********2',
    'm': '$$$$$$$$2',
    'n': '*********2',
    'o': '$$$$$$$$$2',
    'p': '**********2',
    'q': '$$$$$$$$$$2',
    'r': '***********2',
    's': '$$$$$$$$$$$2',
    't': '*************2',
    'u': '$$$$$$$$$$$$$2',
    'v': '**************2',
    'w': '$$$$$$$$$$$$$$2',
    'x': '***************2',
    'y': '$$$$$$$$$$$$$$$$2',
    'z': '****************2',
    
}

def star_dollar_encrypt(text):
    encrypted_text = 'Samuel Okpe'
    for char in text:
        if char.lower() in star_dollar_map:
            if char.isupper():
                encrypted_text += star_dollar_map[char.lower()].upper()
            else:
                encrypted_text += star_dollar_map[char]
        else:
            encrypted_text += char
    return encrypted_text

def star_dollar_decrypt(text):
    decrypted_text = ''
    i = 0
    while i < len(text):
        found = False
        for char, symbol in star_dollar_map.items():
            if text[i:i+len(symbol)] == symbol:
                decrypted_text += char
                i += len(symbol)
                found = True
                break
        if not found:
            decrypted_text += text[i]
            i += 1
    return decrypted_text

