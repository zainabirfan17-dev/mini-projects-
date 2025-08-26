# Function to verify if a credit/debit card number is valid using the Luhn Algorithm
def verify_card_number(card_number):
    sum_of_odd_digits = 0                            # Holds the sum of digits in odd positions
    card_number_reversed = card_number[::-1]         # Reverse the card number (so we start from the right)
    odd_digits = card_number_reversed[::2]           # Take every 2nd digit starting from index 0 (rightmost, odd positions)

    # Add up the digits in odd positions
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0                           # Holds the sum of processed even-position digits
    even_digits = card_number_reversed[1::2]         # Take every 2nd digit starting from index 1 (even positions)

    # Process even-position digits (double them, adjust if >= 10)
    for digit in even_digits:
        number = int(digit) * 2                      # Step 1: double the digit
        if number >= 10:                             # Step 2: if result is 2 digits, add the digits together
            number = (number // 10) + (number % 10)  # Example: 12 → 1 + 2 = 3
        sum_of_even_digits += number                 # Step 3: add result to the running total
    
    # Final total = sum of odd + sum of even
    total = sum_of_odd_digits + sum_of_even_digits
    
    # If divisible by 10, the card number is valid
    return total % 10 == 0


# Main function to test card validation
def main():
    card_number = '4111-1111-4555-1142'              # Example card number (with dashes)
    
    # Create translation table to remove '-' and spaces
    card_translation = str.maketrans({'-': '', ' ': ''})
    
    # Apply translation → get only digits
    translated_card_number = card_number.translate(card_translation)

    # Verify the cleaned card number using Luhn's algorithm
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


# Run the program
main()
