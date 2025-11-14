def verify_card_number(card_number):
    sum_of_odd_digits = 0
    
    # Reverse the number (R-to-L) to correctly identify the checksum digit (first digit)
   
    card_number_reversed = card_number[::-1]
    
    # 1. Sum the odd-positioned digits (1st, 3rd, 5th, etc., from the RIGHT)
    odd_digits = card_number_reversed[::2]

   
    for digit in odd_digits:
        sum_of_odd_digits += int(digit) # FIX: Indented to 8 spaces

    sum_of_even_digits = 0 # FIX: Indented to 4 spaces
    
    # 2. Process the even-positioned digits (2nd, 4th, 6th, etc., from the RIGHT)
    even_digits = card_number_reversed[1::2] 

    
    for digit in even_digits:
        # Double the digit
        number = int(digit) * 2 

        # If doubling results in a number >= 10, sum its digits (e.g., 14 -> 1 + 4 = 5)
        if number >= 10: 
            number = (number // 10) + (number % 10) 

        sum_of_even_digits += number 

    # 3. Calculate the total sum and check for divisibility by 10
    total = sum_of_even_digits + sum_of_odd_digits 
    return 0 == total % 10

def main():
    card_number = '4111-1111-4555-1142'

    card_translation = str.maketrans({'-': '', ' ': ''})

    translated_card_number = card_number.translate(card_translation)

    
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

if __name__ == '__main__':
    main()
