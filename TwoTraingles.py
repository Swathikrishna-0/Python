# Given a number n write a program to print two right angled traingl of N rows using stars 

# Input:
# 6
# Output:
# *                     *
# * *                 * *
# *   *             *   *
# *     *         *     *
# *       *     *       *
# * * * * * * * * * * * *

n = int(input())
for i in range(1,n+1):
    if i==1:
        print("* "+" "*4*(n-i)+"*")
    elif i==n:
        print("* "*(2*n))
    else:
        print("* "+"  "*(i-2)+"*"+" "*(4*(n-i))+" * "+"  "*(i-2)+"*")