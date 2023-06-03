# Write a function with the name alidate_atm_pin_code that takes a word as an argument. 
# ATM PIN is considered valid only if the given word contains 
# -Exactly 4 or 6 characters 
# -All the characters should be digits 

# Input 
# 9837
# Output 
# Valid PIN code 

# Input 
# A289h4
# Output 
# Invalid PIN code

def validate_atm_pin_code(pin):
    length = len(pin)
    is_valid = True
    is_valid_six = (length == 4) or (length ==6)
    if  is_valid_six:
        is_digits = pin.isdigit()
        if not is_digits:
            is_valid = False
    else:
        is_valid = False
        
    if is_valid:
        print("Valid PIN Code")
    else:
        print("Invalid PIN Code")

pin = input()
result = validate_atm_pin_code(pin)
