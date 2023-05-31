# Given an integer N as a starting number and K as input, write a program to print a number pyramid of K rows.

# input 
# 10 
# 5 
# Output 
# 24
# 23 22 
# 21 20 19 
# 18 17 16 15 
# 14 13 12 11 10 
#
# input 
# 1 
# 3
# output 
# 6 
# 5 4 
# 3 2 1
N = int(input())
K = int(input())
counter = N-1
for i in range(K):
    for j in range(i+1):
        counter+=1
for i in range(K):
    for j in range(i+1):
        print(counter,end=" ")
        counter-=1
    print()