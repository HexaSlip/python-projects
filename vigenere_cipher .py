text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    key_lower = key.lower() 

   
    for char in message.lower():

        if char in alphabet:

            # All cipher logic must be indented 12 spaces (inside the if block)
            # 1. Get the current key character, wrapping around the key length
            key_char = key_lower[key_index % len(key_lower)]

            # 2. Get the shift value (offset) from the key character
            offset = alphabet.index(key_char)

            # 3. Advance the key index ONLY for letters
            key_index += 1

            # --- Cipher Logic ---
            index = alphabet.find(char)
            # Use the direction (1 for encrypt, -1 for decrypt)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

        else:
            final_message += char
            # key_index is NOT advanced here

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# --- Execution ---
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')

decryption = decrypt(text, custom_key)
print(f'Decrypted text: {decryption}\n')
