# Given a number n write a program to print a hollow butterfly of 2*N rows using stars 

# Input:
# 4
# Output:
# *             *
# * *         * *
# *   *     *   *
# *     * *     *
# *     * *     *
# *   *     *   *
# * *         * *
# *             *

n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,2*n-2*i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1 or j==i:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
    
for i in range(n,0,-1):
    for j in range(1,i+1):
        if j==1 or j==i:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,2*n-2*i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
            
            
            
            
            
            
            
            
            
            
            
            
            
            