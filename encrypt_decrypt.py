# Vigenère Cipher Implementation in Python
# Author: Zainab
# This program allows a user to encrypt or decrypt messages using a simple Vigenère cipher.

# Get the input message from the user
message = input("Enter the message you want to encrypt or decrypt: ")

# Define the alphabet as the key space
key = "abcdefghijklmnopqrstuvwxyz"

# Ask the user whether they want to encrypt or decrypt
mode = input("Do you want to encrypt (E) or decrypt (D)?: ").upper()

def vigenere(message, key, mode):
    """
    Encrypts or decrypts a message using a simple Vigenère cipher.

    Parameters:
        message (str): The input text to encrypt or decrypt.
        key (str): The alphabet string used as the key space.
        mode (str): Either "E" for encryption or "D" for decryption.

    Returns:
        str: The encrypted or decrypted text.
    """
    key_index = 0            # Keeps track of the current position in the key
    final_message = ""       # Stores the result
    direction = 1 if mode == "E" else -1  # Encryption = +1, Decryption = -1

    for char in message.lower():  # Process each character in the message
        if not char.isalpha():
            # Non-alphabet characters are added as-is (spaces, punctuation, etc.)
            final_message += char
        else:
            # Get the corresponding key character (cycling through the key)
            key_char = key[key_index % len(key)]
            key_index += 1

            # Find the shift value (offset) from the key character
            offset = key.index(key_char)

            # Find the current index of the character in the alphabet
            index = key.index(char)

            # Apply the shift (forward for encryption, backward for decryption)
            new_index = (index + offset * direction) % len(key)

            # Add the new encrypted/decrypted character to the result
            final_message += key[new_index]

    return final_message

# Run the cipher function and display results
result = vigenere(message, key, mode)
print(f"Text : {message} \nMode : {mode} \nFinal Message : {result}")
