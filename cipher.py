# Example ciphertext and key
text ='ty cpkg wv hnouaq'
custom_key = 'happycoding'

# Vigenère cipher function
def vigenere(message, key, direction=1):
    key_index = 0                          # Keeps track of which letter in the key to use
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # The allowed alphabet
    final_message = ''                     # Stores the resulting encrypted/decrypted text
    
    # Loop through every character in the message
    for char in message.lower():
        
        # If the character is not a letter (like spaces, punctuation), add it directly
        if not char.isalpha():
            final_message += char
        else:        
            # Pick the current key character (repeats key when needed)
            key_char = key[key_index % len(key)]
            key_index += 1

            # Find the "shift amount" (offset) based on key character position in alphabet
            offset = alphabet.index(key_char)

            # Find the index of the current message character in the alphabet
            index = alphabet.find(char)

            # Calculate the new index:
            #   For encryption → add offset
            #   For decryption → subtract offset (direction = -1)
            new_index = (index + offset * direction) % len(alphabet)

            # Append the new shifted character to the final message
            final_message += alphabet[new_index]
    
    return final_message

# Encrypt using default direction (1 → forward shift)
def encrypt(message, key):
    return vigenere(message, key)

# Decrypt using reverse direction (-1 → backward shift)
def decrypt(message, key):
    return vigenere(message, key, -1)

# Example run
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)  # Decrypt the given ciphertext
print(f'\nDecrypted text: {decryption}\n')
