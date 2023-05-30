# Given N number of days as input write a program to convert N number of days to years, weeks and days.

# take 1 year = 365days

# N = 1329 
# 1329 = 3years + 33weeks + 3days 

# so output should be 

# o/p -> 3 
#        33 
#        3

N = int(input())
days_in_week = 7 
Y = int(N/365)
W = int((N%365) / days_in_week)
D = int((N%365)% days_in_week)
print(Y)
print(W)
print(D)