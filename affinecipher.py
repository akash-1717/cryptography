def encrypt(plaintext, a, b):
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            else:
                encrypted_char = chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
        else:
            encrypted_char = char
        
        ciphertext += encrypted_char
    
    return ciphertext


def decrypt(ciphertext, a, b):
    plaintext = ""
    
    mod_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            mod_inverse = i
            break
    
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((mod_inverse * (ord(char) - ord('A') - b)) % 26 + ord('A'))
            else:
                decrypted_char = chr((mod_inverse * (ord(char) - ord('a') - b)) % 26 + ord('a'))
        else:
            decrypted_char = char
        
        plaintext += decrypted_char
    
    return plaintext


plaintext = "Hello, World!"
a = 5
b = 8

ciphertext = encrypt(plaintext, a, b)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext, a, b)
print("Decrypted text:", decrypted_text)


# output:
# Ciphertext: Mjqqt, Btwqi!
# Decrypted text: Hello, World!
