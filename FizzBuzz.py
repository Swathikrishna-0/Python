# write a function with the name fixx_buzz that takes a number as an argument. 
# - If the number is divisible by 3, it should return 'Fizz'
# -If it is divisible by 5, it should return 'Fizz'
# - If it is divisible by both 3 and 5, it should return "FizzBuzz"
# -Otherwise, it should return the same number.

# Input 
# 20 
# Output 
# Buzz 

# Input 
# 7 
# Output 
# 7 

def fizz_buzz(number):
    is_div_by_3 = (number%3)==0
    is_div_by_5 = (number%5)==0
    is_div_by_both = is_div_by_5 and is_div_by_3
    if is_div_by_both:
        msg = "FizzBuzz"
    elif is_div_by_3:
        msg = "Fizz"
    elif is_div_by_5:
        msg = "Buzz"
    else:
        msg = number
    return msg

number = int(input())
final = fizz_buzz(number)
print(final)

