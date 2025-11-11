"""

Write a python Program to check entered password by user
is correct or not. Entered password is correct if it has upper
character, lower character , digits (but not more than 3 digits),
special character and length is greater than or equal to
eight and less than equal to fifteen. Get the digits from
entered password and convert it in to number and then convert it
in to English Word .

"""

def is_length_valid(pas):
    return len(pas) >= 8 and len(pas) <= 15

def is_case_valid(pas):
    return not(pas.islower()) and not(pas.isupper())

def has_digit(pas):
    dig_count = 0
    for i in pas:
        if i.isdigit():
            dig_count += 1

    return dig_count in (1, 2, 3)

def has_special(pas):
    for i in pas:
        if i in ('!@#$%^&*'):
            return True

    return False

def print_digits(pas):
    num = ''
    
    # Extract all digits from password
    for i in pas:
        if i.isdigit():
            num += i

    print(f"num = {num}")
    
    # Dictionary for single digits
    words = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', 
             '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    
    # Dictionary for tens (20-90)
    words_tens = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
                  '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
    
    # Dictionary for teens (10-19)
    words_teens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
                   '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', 
                   '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
    
    num_words = ''


    # remove leading zeors
    while num[0] == '0':
        num = num[1:]
        if len(num) == 0:
            break
    
    # Handle 3-digit numbers
    if len(num) == 3:

        num_words = words[num[0]] + ' hundred'
        if num[1:] != '00':
            num_words += ' and '
        num = num[1:]  # Remove hundreds digit
    
    # Handle 2-digit numbers (including teens)
    if len(num) == 2:
        
        if num[0] == '1':  # Teens (10-19)
            num_words += words_teens[num]
            num = ''  # Fully processed

        elif num[0] != '0':  # 20-99
            num_words += words_tens[num[0]]
            if num[1] != '0':
                num_words += '-' + words[num[1]]
            num = ''  # Fully processed

        else:  # Leading zero (e.g., 01, 02)
            if num[1] != '0':
                num_words += words[num[1]]
            num = ''
    
    # Handle single digit and no digits
    if len(num) == 1:
        num_words += words[num]

    num_words = "Zero" if len(num_words) == 0 else num_words
    
    print(f"Num in words: {num_words.strip()}")


password = input("Enter your password: ")
    
    
if not is_length_valid(password):
    print("Password length must be between 8 and 15 characters")
    
else:
    if not is_case_valid(password):
        print("Password must contain both uppercase and lowercase characters")
    
    else:
        if not has_digit(password):
            print("Password must contain 1 to 3 digits")
    
        else:
            if not has_special(password):
                print("Password must contain at least one special character (!@#$%^&*)")
            
            else:
                print("Password is valid")

                print_digits(password)