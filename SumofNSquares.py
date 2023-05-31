# Write a program that reads a number N and prints the sum of squares of N numbers starting from 1.

# input 
# 4 
# output 
# 30 

# input 
# 7 
# output 
# 140 

n = int(input())
arr = []
for i in range(1,n+1):
    arr.append(i**2)
    i = i + 1 
res = 0
for i in arr:
    res = res + i 
print(res)