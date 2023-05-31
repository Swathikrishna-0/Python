# Given two numbers X and N write a program to print the sum of N terms in the given series. 
# series: 
# X, -X^3, X^5, -X^7, X^9, .... N terms 
# input 
# 2
# 5
# output 
# 2+(-2^3)+2^5+(-2^7)+2^9 
# 2+(-8)+32+(-128)+512 = 410 
x = int(input())
n = int(input())
sum = 0
power = 1
for i in range(n):
	sum += power*(x**(2*i+1))
	power *= -1
print(sum)