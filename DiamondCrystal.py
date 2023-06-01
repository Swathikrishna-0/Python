# Diamond Crystal 
# Given an integer value N, write a program to print a diamond pattern of 2*N rows as shown below.

# input 
# 3
# output 
#   /\
#  /  \
# /    \
# \    /
#  \  /
#   \/

N = int(input())
for i in range(0,N):
    print(' '*(N-i-1)+'/'+' '*(2*i)+'\\')
for i in range(0,N):
    print(' '*(i)+'\\'+' '*(2*(N-i-1))+'/')
