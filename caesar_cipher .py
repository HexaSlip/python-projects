### Previous Caesar Cipher Code

def caesar(message, offset):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message:

        # 1. Check if the character is a letter
        if char.isalpha():
            is_upper = char.isupper()
            char_lower = char.lower()

            #Find the position (index) of the letter
            index = alphabet.find(char_lower) 

            # 2. Apply the shift with modulus (wrap-around) 
            new_index = (index + offset) % len(alphabet)
            new_char = alphabet[new_index] 
            
            # 3. Preserve the original case
            if is_upper:
                encrypted_text += new_char.upper() 
            else: 
                encrypted_text += new_char
        # 4. Handle ALL non-alphabetic characters (spaces, punctuation, numbers)
        else: 
            encrypted_text += char
    return encrypted_text # Return the result for reusability

# --- Execution ---
text = 'Hello Zaira'
shift = 3

encrypted_shift_3 = caesar(text, shift)
encrypted_shift_13 = caesar(text, 13)

print('--- Caesar Cipher Results ---')
print(f'Plain Text: {text}') 
print(f'Shift{shift}: {encrypted_shift_3}')
print(f'Shift 13: {encrypted_shift_13}')
