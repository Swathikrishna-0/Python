# Write a program that reads a two-digit number N and checks if N is divisible by both the digits of N. 
# Print the double of N if N is divisible by both the digits of N. Otherwise print N. 

# Input
# 15 
# Output 
# 15%1 == 0 
# 15%5 == 0
# 15*2 = 30 

# Input 
# 26 
# Output 
# 26%2 == 0
# 26%6 != 0 
# 26
word = input()
first3 = word[0:3]
nxt = (first3 =="NXT")
div2 = (int(word[3:]))%2 ==0
div7 = (int(word[3:]))%7 ==0
if (nxt) and (div2 or div7):
    print("Special String")
else:
    print("Not a Special String")