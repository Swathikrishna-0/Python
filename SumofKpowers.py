# Write a program that reads two numbers N and K and prints the sum of the Kth power of all the numbers from 1 to N 
# n = 5 k = 3 
# 1^3+2^3+3^3+4^3+5^3 
# input 
# 2 
# 8 
# output 
# 257 
n = int(input())
k = int(input())
sum = 0 
for i in range(1,n+1):
    sum = sum + i**k
print(sum)
    